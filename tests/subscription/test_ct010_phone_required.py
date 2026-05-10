"""
CT010 — Required "Telefone" field (docs/test-cases.md, personal data).

Objective:
    The user cannot proceed with an empty phone number.

Preconditions:
    ``go_to_personal_data_step`` in ``utils/subscription_steps.py``.

UI note:
    An empty or too-short value shows ``Telefone inválido.`` (minimum length / Zod), blocking advance.

Flake risks:
    - Age combobox: close after selecting the range before clicking Next.
"""

from __future__ import annotations

from playwright.sync_api import Page, expect

from data.subscription_data import (
    SUBSCRIPTION_EMAIL,
    SUBSCRIPTION_IDADE_FAIXA_OPTION,
    SUBSCRIPTION_NOME_BEBE,
    SUBSCRIPTION_NOME_COMPLETO,
    VALIDATION_MSG_TELEFONE_OBRIGATORIO,
)
from utils.navigation import expect_subscribe_url
from utils.subscription_steps import (
    click_next,
    expect_personal_data_step,
    go_to_personal_data_step,
)


def test_ct010_empty_phone_blocks_progress(page: Page):
    go_to_personal_data_step(page)
    personal_data_heading = expect_personal_data_step(page)

    telefone = page.get_by_label("Telefone")

    page.get_by_label("Nome Completo").fill(SUBSCRIPTION_NOME_COMPLETO)
    page.get_by_label("E-mail").fill(SUBSCRIPTION_EMAIL)
    page.get_by_label("Nome do Bebê").fill(SUBSCRIPTION_NOME_BEBE)

    page.get_by_label("Idade do Bebê").click()
    page.get_by_role("option", name=SUBSCRIPTION_IDADE_FAIXA_OPTION).click()

    expect(telefone).to_be_visible()
    expect(telefone).to_have_value("")

    click_next(page)

    expect(page.get_by_text(VALIDATION_MSG_TELEFONE_OBRIGATORIO, exact=True)).to_be_visible()
    expect(personal_data_heading).to_be_visible()
    expect(telefone).to_be_visible()
    expect_subscribe_url(page)
