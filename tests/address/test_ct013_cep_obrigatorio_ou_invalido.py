"""
CT013 — Validar CEP obrigatório ou inválido (test-cases.md).

Pré-condições: etapa "Endereço de Entrega" via `go_to_address_step` em utils/address_steps.py.

Cenários:
- CEP em branco: a UI reutiliza a mensagem de CEP inválido (mesmo padrão de outros campos com Zod).
- CEP com formato inválido: mesma mensagem, sem depender de API de busca de CEP.

Riscos de flake:
- Outros erros de endereço podem aparecer quando o CEP está vazio; o teste valida explicitamente a mensagem do CEP.
"""

from __future__ import annotations

from playwright.sync_api import Page, expect

from data.address_data import ADDRESS_CEP_MALFORMED, VALIDATION_MSG_CEP_INVALIDO
from utils.address_steps import expect_endereco_entrega_step, go_to_address_step
from utils.navigation import expect_subscribe_url
from utils.subscription_steps import click_avancar


def test_ct013_cep_vazio_impede_avanco_e_exibe_erro(page: Page):
    go_to_address_step(page)
    endereco = expect_endereco_entrega_step(page)

    cep = page.get_by_label("CEP")
    expect(cep).to_be_visible()
    expect(cep).to_have_value("")

    click_avancar(page)

    expect(page.get_by_text(VALIDATION_MSG_CEP_INVALIDO, exact=True)).to_be_visible()
    expect(endereco).to_be_visible()
    expect(cep).to_be_visible()
    expect_subscribe_url(page)


def test_ct013_cep_formato_invalido_impede_avanco_e_exibe_erro(page: Page):
    go_to_address_step(page)
    endereco = expect_endereco_entrega_step(page)

    cep = page.get_by_label("CEP")
    cep.fill(ADDRESS_CEP_MALFORMED)
    expect(cep).to_have_value(ADDRESS_CEP_MALFORMED)

    click_avancar(page)

    expect(page.get_by_text(VALIDATION_MSG_CEP_INVALIDO, exact=True)).to_be_visible()
    expect(endereco).to_be_visible()
    expect(cep).to_be_visible()
    expect_subscribe_url(page)
