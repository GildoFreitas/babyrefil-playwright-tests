"""
CT011 — Validar campo "Nome do Bebê" obrigatório (test-cases.md).

Pré-condições: `go_to_personal_data_step` em utils/subscription_steps.py.

Riscos de flake:
- Ao avançar sem nome do bebê, a UI pode exibir outros erros de endereço; o teste valida a
  mensagem específica do nome do bebê.
"""

from __future__ import annotations

import re

from playwright.sync_api import Page, expect

from data.subscription_data import (
    SUBSCRIPTION_EMAIL,
    SUBSCRIPTION_IDADE_FAIXA_OPTION,
    SUBSCRIPTION_NOME_COMPLETO,
    SUBSCRIPTION_TELEFONE,
    VALIDATION_MSG_NOME_BEBE_OBRIGATORIO,
)
from utils.env import get_base_url
from utils.subscription_steps import (
    click_avancar,
    expect_dados_pessoais_step,
    go_to_personal_data_step,
)


def test_ct011_nome_bebe_vazio_impede_avanco_e_exibe_erro(page: Page):
    base = get_base_url()

    go_to_personal_data_step(page)
    dados_pessoais = expect_dados_pessoais_step(page)

    nome_bebe = page.get_by_label("Nome do Bebê")

    page.get_by_label("Nome Completo").fill(SUBSCRIPTION_NOME_COMPLETO)
    page.get_by_label("E-mail").fill(SUBSCRIPTION_EMAIL)
    page.get_by_label("Telefone").fill(SUBSCRIPTION_TELEFONE)

    page.get_by_label("Idade do Bebê").click()
    page.get_by_role("option", name=SUBSCRIPTION_IDADE_FAIXA_OPTION).click()

    expect(nome_bebe).to_be_visible()
    expect(nome_bebe).to_have_value("")

    click_avancar(page)

    expect(page.get_by_text(VALIDATION_MSG_NOME_BEBE_OBRIGATORIO, exact=True)).to_be_visible()
    expect(dados_pessoais).to_be_visible()
    expect(nome_bebe).to_be_visible()
    expect(page).to_have_url(re.compile(re.escape(base) + r"/subscribe/?$"))
