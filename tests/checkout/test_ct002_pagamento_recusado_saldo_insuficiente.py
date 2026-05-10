"""
CT002 — Checkout fails with insufficient funds (docs/test-cases.md, checkout flow).

Objective:
    Validate behavior when payment is declined for insufficient funds.

Preconditions:
    The Payment step is reached via ``go_to_payment_step`` in ``utils/payment_steps.py``
    (Plan → Recurrence → Personal data → Address with the default data set).

Scenario:
    Insufficient-funds Mastercard (``PAYMENT_CARD_MASTERCARD_SALDO_INSUFICIENTE``) → payment
    is declined, a toast shows ``PAYMENT_MSG_TRANSACAO_NAO_AUTORIZADA``, and the user stays
    on the payment step.

Flake risks:
    - Toast appears after the simulated gateway response; default ``expect`` timeout is usually enough.
    - Multiple toasts can stack; the test uses the exact expected message string.
"""

from __future__ import annotations

from playwright.sync_api import Page, expect

from data.payment_data import (
    PAYMENT_CARD_MASTERCARD_SALDO_INSUFICIENTE,
    PAYMENT_MSG_TRANSACAO_NAO_AUTORIZADA,
)
from utils.navigation import expect_subscribe_url
from utils.payment_steps import (
    click_finalizar_assinatura,
    expect_pagamento_step,
    fill_cartao,
    go_to_payment_step,
)


def test_ct002_pagamento_recusado_saldo_insuficiente(page: Page):
    go_to_payment_step(page)
    finalizar = expect_pagamento_step(page)

    fill_cartao(page, numero=PAYMENT_CARD_MASTERCARD_SALDO_INSUFICIENTE)
    click_finalizar_assinatura(page)

    expect(page.get_by_text(PAYMENT_MSG_TRANSACAO_NAO_AUTORIZADA, exact=True)).to_be_visible()

    expect(finalizar).to_be_visible()
    expect_subscribe_url(page)
