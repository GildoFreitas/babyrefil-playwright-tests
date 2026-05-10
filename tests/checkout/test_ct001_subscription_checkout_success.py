"""
CT001 — Successful subscription checkout (docs/test-cases.md, checkout flow).

Objective:
    Validate the end-to-end subscription flow with valid data.

Preconditions:
    The Payment step is reached via ``go_to_payment_step`` in ``utils/payment_steps.py``
    (Plan → Recurrence → Personal data → Address with the default data set).

Scenario:
    Valid Visa card (``PAYMENT_CARD_VISA_VALIDO``) → payment is approved and the confirmation
    screen shows:
    - h1 ``Assinatura confirmada!``
    - ``Resumo do seu pedido`` + order number matching ``PAYMENT_PEDIDO_NUMERO_REGEX``
    - Summary headings: ``Plano``, ``Frequência``, ``Endereço de Entrega``, ``Próxima Entrega``
    - Estimated delivery date in pt-BR long form (``PAYMENT_DATA_ENTREGA_REGEX``)
    
Flake risks:
    - Order number is dynamic (e.g. timestamp); assert format via regex, not an exact string.
    - Long-form date changes daily; assert using the ``<day> de <month> de <year>`` pattern.
"""

from __future__ import annotations

from playwright.sync_api import Page, expect

from data.payment_data import (
    PAYMENT_CARD_VISA_VALIDO,
    PAYMENT_DATA_ENTREGA_REGEX,
)
from utils.payment_steps import (
    click_finish_subscription,
    expect_subscription_confirmed,
    expect_payment_step,
    fill_card_form,
    go_to_payment_step,
)


def test_ct001_successful_checkout_end_to_end(page: Page):
    go_to_payment_step(page)
    expect_payment_step(page)

    fill_card_form(page, card_number=PAYMENT_CARD_VISA_VALIDO)
    click_finish_subscription(page)

    confirmed_heading = expect_subscription_confirmed(page)

    for heading in ("Plano", "Frequência", "Endereço de Entrega", "Próxima Entrega"):
        expect(page.get_by_role("heading", name=heading, level=3)).to_be_visible()

    expect(page.get_by_text(PAYMENT_DATA_ENTREGA_REGEX)).to_be_visible()
    expect(confirmed_heading).to_be_visible()
