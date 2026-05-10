"""
CT016 — Required / invalid payment fields (docs/test-cases.md, payment).

Objective:
    Subscription cannot complete without valid card data; validation messages appear.

Preconditions:
    Payment step via ``go_to_payment_step`` in ``utils/payment_steps.py``
    (Plan → Recurrence → Personal data → Address with default data).

Scenarios (aligned with case data):
    - All card fields empty: all five form error messages.
    - Invalid non-empty values: same messages (per-field Zod) without hitting the payment gateway.

Flake risks:
    - The word ``Pagamento`` appears in the step indicator and section title; the step checkpoint
      uses ``Resumo do Pedido`` + ``Finalizar Assinatura`` (``expect_payment_step``).
    - Messages sit near fields; assertions use exact UI strings to avoid brittle DOM coupling.
"""

from __future__ import annotations

from playwright.sync_api import Page, expect

from data.payment_data import (
    PAYMENT_CARD_NUMBER_INVALIDO,
    PAYMENT_CPF_INVALIDO,
    PAYMENT_CVV_INVALIDO,
    PAYMENT_VALIDADE_INVALIDA,
    VALIDATION_MSG_CARD_NUMBER_INVALIDO,
    VALIDATION_MSG_CPF_INVALIDO,
    VALIDATION_MSG_CVV_INVALIDO,
    VALIDATION_MSG_NOME_CARTAO_OBRIGATORIO,
    VALIDATION_MSG_VALIDADE_INVALIDA,
)
from utils.navigation import expect_subscribe_url
from utils.payment_steps import (
    click_finish_subscription,
    expect_payment_step,
    go_to_payment_step,
)

_VALIDATION_MESSAGES = (
    VALIDATION_MSG_CARD_NUMBER_INVALIDO,
    VALIDATION_MSG_NOME_CARTAO_OBRIGATORIO,
    VALIDATION_MSG_VALIDADE_INVALIDA,
    VALIDATION_MSG_CVV_INVALIDO,
    VALIDATION_MSG_CPF_INVALIDO,
)


def test_ct016_empty_card_fields_show_validation(page: Page):
    go_to_payment_step(page)
    finish_button = expect_payment_step(page)

    card_number_field = page.get_by_label("Número do Cartão")
    cardholder_name_field = page.get_by_label("Nome no Cartão")
    expiry_field = page.get_by_label("Validade")
    cvv_field = page.get_by_label("CVV")
    cpf_field = page.get_by_label("CPF do Titular")

    for field in (card_number_field, cardholder_name_field, expiry_field, cvv_field, cpf_field):
        expect(field).to_be_visible()
        expect(field).to_have_value("")

    click_finish_subscription(page)

    for msg in _VALIDATION_MESSAGES:
        expect(page.get_by_text(msg, exact=True)).to_be_visible()

    expect(finish_button).to_be_visible()
    expect_subscribe_url(page)


def test_ct016_invalid_card_fields_show_validation(page: Page):
    go_to_payment_step(page)
    finish_button = expect_payment_step(page)

    page.get_by_label("Número do Cartão").fill(PAYMENT_CARD_NUMBER_INVALIDO)
    page.get_by_label("Validade").fill(PAYMENT_VALIDADE_INVALIDA)
    page.get_by_label("CVV").fill(PAYMENT_CVV_INVALIDO)
    page.get_by_label("CPF do Titular").fill(PAYMENT_CPF_INVALIDO)
    expect(page.get_by_label("Nome no Cartão")).to_have_value("")

    click_finish_subscription(page)

    for msg in _VALIDATION_MESSAGES:
        expect(page.get_by_text(msg, exact=True)).to_be_visible()

    expect(finish_button).to_be_visible()
    expect_subscribe_url(page)
