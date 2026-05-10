"""
CT008 — Required "Nome Completo" field (docs/test-cases.md, personal data).

Objective:
    The user cannot proceed without filling full name; the expected validation message is shown.

Preconditions:
    ``go_to_personal_data_step`` in ``utils/subscription_steps.py`` (home → subscribe → plan →
    monthly recurrence → personal data screen).

Flake risks:
    - Age combobox: select the option before clicking Next.
    - Monthly radio is visually hidden; handled in ``select_monthly_delivery_frequency``.
"""

from __future__ import annotations

from playwright.sync_api import Page, expect

from data.subscription_data import (
    SUBSCRIPTION_EMAIL,
    SUBSCRIPTION_IDADE_FAIXA_OPTION,
    SUBSCRIPTION_NOME_BEBE,
    SUBSCRIPTION_TELEFONE,
    VALIDATION_MSG_NOME_COMPLETO_OBRIGATORIO,
)
from utils.navigation import expect_subscribe_url
from utils.subscription_steps import (
    click_next,
    expect_personal_data_step,
    go_to_personal_data_step,
)


def test_ct008_empty_full_name_blocks_progress(page: Page):
    go_to_personal_data_step(page)
    personal_data_heading = expect_personal_data_step(page)

    nome_completo = page.get_by_label("Nome Completo")

    page.get_by_label("E-mail").fill(SUBSCRIPTION_EMAIL)
    page.get_by_label("Telefone").fill(SUBSCRIPTION_TELEFONE)
    page.get_by_label("Nome do Bebê").fill(SUBSCRIPTION_NOME_BEBE)

    page.get_by_label("Idade do Bebê").click()
    page.get_by_role("option", name=SUBSCRIPTION_IDADE_FAIXA_OPTION).click()

    expect(nome_completo).to_be_visible()
    expect(nome_completo).to_have_value("")

    click_next(page)

    expect(page.get_by_text(VALIDATION_MSG_NOME_COMPLETO_OBRIGATORIO, exact=True)).to_be_visible()
    expect(personal_data_heading).to_be_visible()
    expect(nome_completo).to_be_visible()
    expect_subscribe_url(page)
