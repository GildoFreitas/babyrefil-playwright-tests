"""
CT012 — Required "Idade do Bebê" field (docs/test-cases.md, personal data).

Objective:
    The user cannot proceed without selecting the baby's age range.

Preconditions:
    ``go_to_personal_data_step`` in ``utils/subscription_steps.py``.

Data:
    Age not selected — combobox keeps the placeholder (``SUBSCRIPTION_IDADE_PLACEHOLDER``).

Flake risks:
    - Address or other errors may appear together; the test asserts only the age validation message.
"""

from __future__ import annotations

from playwright.sync_api import Page, expect

from data.subscription_data import (
    SUBSCRIPTION_EMAIL,
    SUBSCRIPTION_IDADE_PLACEHOLDER,
    SUBSCRIPTION_NOME_BEBE,
    SUBSCRIPTION_NOME_COMPLETO,
    SUBSCRIPTION_TELEFONE,
    VALIDATION_MSG_IDADE_BEBE_OBRIGATORIA,
)
from utils.navigation import expect_subscribe_url
from utils.subscription_steps import (
    click_avancar,
    expect_dados_pessoais_step,
    go_to_personal_data_step,
)


def test_ct012_idade_bebe_nao_selecionada_impede_avanco_e_exibe_erro(page: Page):
    go_to_personal_data_step(page)
    dados_pessoais = expect_dados_pessoais_step(page)

    idade = page.get_by_role("combobox", name="Idade do Bebê")

    page.get_by_label("Nome Completo").fill(SUBSCRIPTION_NOME_COMPLETO)
    page.get_by_label("E-mail").fill(SUBSCRIPTION_EMAIL)
    page.get_by_label("Telefone").fill(SUBSCRIPTION_TELEFONE)
    page.get_by_label("Nome do Bebê").fill(SUBSCRIPTION_NOME_BEBE)

    expect(idade).to_be_visible()
    expect(idade).to_contain_text(SUBSCRIPTION_IDADE_PLACEHOLDER)

    click_avancar(page)

    expect(page.get_by_text(VALIDATION_MSG_IDADE_BEBE_OBRIGATORIA, exact=True)).to_be_visible()
    expect(dados_pessoais).to_be_visible()
    expect(idade).to_be_visible()
    expect_subscribe_url(page)
