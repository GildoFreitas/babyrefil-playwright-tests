"""
Passos reutilizáveis até a etapa "Endereço de Entrega" no /subscribe.

Reutiliza a navegação inicial de `subscription_steps` (banner → plano → mensal → dados pessoais),
em seguida preenche a massa padrão de dados pessoais/bebê e avança até o bloco de CEP/endereço.
"""

from __future__ import annotations

import re

from playwright.sync_api import Locator, Page, expect

from data.address_data import (
    ADDRESS_CEP_VALIDO_AUTOCOMPLETE,
    ADDRESS_COMPLEMENTO,
    ADDRESS_NUMERO,
)
from data.subscription_data import (
    SUBSCRIPTION_EMAIL,
    SUBSCRIPTION_IDADE_FAIXA_OPTION,
    SUBSCRIPTION_NOME_BEBE,
    SUBSCRIPTION_NOME_COMPLETO,
    SUBSCRIPTION_TELEFONE,
)
from utils.subscription_steps import (
    click_avancar,
    expect_dados_pessoais_step,
    go_to_personal_data_step,
)


def expect_endereco_entrega_step(page: Page) -> Locator:
    """Checkpoint: seção Endereço de Entrega visível (heading nível 3)."""
    endereco = page.get_by_role("heading", name="Endereço de Entrega", level=3)
    expect(endereco).to_be_visible()
    return endereco


def go_to_address_step(page: Page) -> None:
    """
    Abre /subscribe, percorre até a tela "Seus Dados" e preenche Dados Pessoais + Bebê.

    A tela "Seus Dados" engloba Dados Pessoais, Dados do Bebê e Endereço de Entrega na mesma
    página, com um único Avançar que valida o form inteiro (Zod) e leva direto a Pagamento.
    Por isso NÃO clicamos Avançar aqui — a seção de Endereço já está visível desde a chegada
    nessa tela. Clicar Avançar antes do endereço estar preenchido dispara um flash de erros
    nos campos de endereço (sem efeito funcional, apenas cosmético).
    """
    go_to_personal_data_step(page)
    expect_dados_pessoais_step(page)

    page.get_by_label("Nome Completo").fill(SUBSCRIPTION_NOME_COMPLETO)
    page.get_by_label("E-mail").fill(SUBSCRIPTION_EMAIL)
    page.get_by_label("Telefone").fill(SUBSCRIPTION_TELEFONE)
    page.get_by_label("Nome do Bebê").fill(SUBSCRIPTION_NOME_BEBE)

    page.get_by_label("Idade do Bebê").click()
    page.get_by_role("option", name=SUBSCRIPTION_IDADE_FAIXA_OPTION).click()

    expect_endereco_entrega_step(page)


def buscar_endereco_por_cep(page: Page, cep: str) -> None:
    """
    Informa o CEP, clica em Buscar e aguarda o logradouro retornado pela API (campo Rua habilitado e preenchido).
    """
    page.get_by_label("CEP").fill(cep)
    buscar = page.get_by_role("button", name="Buscar")
    expect(buscar.first).to_be_visible()
    expect(buscar.first).to_be_enabled()
    buscar.first.click()
    rua = page.get_by_label("Rua")
    # A UI pode manter o logradouro desabilitado após a busca; basta aguardar o valor da API.
    expect(rua).to_have_value(re.compile(r"\S"), timeout=20_000)


def complete_endereco_step(page: Page) -> None:
    """
    Conclui a etapa de endereço com a massa padrão (CEP + autocomplete + Número/Complemento)
    e clica em Avançar. Pré-requisito: já estar na etapa "Endereço de Entrega".
    """
    buscar_endereco_por_cep(page, ADDRESS_CEP_VALIDO_AUTOCOMPLETE)
    page.get_by_label("Número").fill(ADDRESS_NUMERO)
    page.get_by_label("Complemento (Opcional)").fill(ADDRESS_COMPLEMENTO)
    click_avancar(page)
