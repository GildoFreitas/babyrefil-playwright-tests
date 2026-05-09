"""
CT009 — Validar campo "E-mail" obrigatório (test-cases.md).

Pré-condições: `go_to_personal_data_step` em utils/subscription_steps.py.

Nota: com o campo vazio, a UI exibe "E-mail inválido." (validação de formato / Zod), o que
ainda impede o avanço e atende ao objetivo do caso.

Riscos de flake:
- Combobox idade: fechar após selecionar a faixa antes de Avançar.
"""

from __future__ import annotations

from playwright.sync_api import Page, expect

from data.subscription_data import (
    SUBSCRIPTION_IDADE_FAIXA_OPTION,
    SUBSCRIPTION_NOME_BEBE,
    SUBSCRIPTION_NOME_COMPLETO,
    SUBSCRIPTION_TELEFONE,
    VALIDATION_MSG_EMAIL_OBRIGATORIO,
)
from utils.navigation import expect_subscribe_url
from utils.subscription_steps import (
    click_avancar,
    expect_dados_pessoais_step,
    go_to_personal_data_step,
)


def test_ct009_email_vazio_impede_avanco_e_exibe_erro(page: Page):
    go_to_personal_data_step(page)
    dados_pessoais = expect_dados_pessoais_step(page)

    email = page.get_by_label("E-mail")

    page.get_by_label("Nome Completo").fill(SUBSCRIPTION_NOME_COMPLETO)
    page.get_by_label("Telefone").fill(SUBSCRIPTION_TELEFONE)
    page.get_by_label("Nome do Bebê").fill(SUBSCRIPTION_NOME_BEBE)

    page.get_by_label("Idade do Bebê").click()
    page.get_by_role("option", name=SUBSCRIPTION_IDADE_FAIXA_OPTION).click()

    expect(email).to_be_visible()
    expect(email).to_have_value("")

    click_avancar(page)

    expect(page.get_by_text(VALIDATION_MSG_EMAIL_OBRIGATORIO, exact=True)).to_be_visible()
    expect(dados_pessoais).to_be_visible()
    expect(email).to_be_visible()
    expect_subscribe_url(page)
