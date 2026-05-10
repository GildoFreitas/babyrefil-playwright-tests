"""
Steps up to the Payment step on ``/subscribe``.

Uses ``go_to_address_step`` (subscription → personal data → address) and ``complete_address_step``
with the default data set to reach the last wizard stage.

Stable locators (MCP snapshot):
    - Payment: ``Resumo do Pedido`` + button ``Finalizar Assinatura`` (single CTA for the step).
    - Card fields (labels): ``Número do Cartão``, ``Nome no Cartão``, ``Validade``, ``CVV``, ``CPF do Titular``.
"""

from __future__ import annotations

from playwright.sync_api import Locator, Page, expect

from data.payment_data import (
    PAYMENT_CPF,
    PAYMENT_CVV,
    PAYMENT_NOME_TITULAR,
    PAYMENT_PEDIDO_NUMERO_REGEX,
    PAYMENT_VALIDADE_FUTURA,
)
from utils.address_steps import complete_address_step, go_to_address_step


def expect_payment_step(page: Page) -> Locator:
    """
    Checkpoint: payment step visible.

    Anchors on ``Resumo do Pedido`` + ``Finalizar Assinatura`` — the word ``Pagamento`` is duplicated
    (stepper + section title), so it is not used as the sole locator.
    """
    expect(page.get_by_text("Resumo do Pedido", exact=True)).to_be_visible()
    finish = page.get_by_role("button", name="Finalizar Assinatura")
    expect(finish).to_be_visible()
    return finish


def go_to_payment_step(page: Page) -> None:
    """Open subscribe flow through address (default data) until the payment form is shown."""
    go_to_address_step(page)
    complete_address_step(page)
    expect_payment_step(page)


def click_finish_subscription(page: Page) -> None:
    """Click ``Finalizar Assinatura`` on the payment step."""
    finish = page.get_by_role("button", name="Finalizar Assinatura")
    expect(finish).to_be_visible()
    expect(finish).to_be_enabled()
    finish.click()


def fill_card_form(page: Page, *, card_number: str) -> None:
    """Fill card form with default holder data; only ``card_number`` varies by scenario."""
    page.get_by_label("Número do Cartão").fill(card_number)
    page.get_by_label("Nome no Cartão").fill(PAYMENT_NOME_TITULAR)
    page.get_by_label("Validade").fill(PAYMENT_VALIDADE_FUTURA)
    page.get_by_label("CVV").fill(PAYMENT_CVV)
    page.get_by_label("CPF do Titular").fill(PAYMENT_CPF)


def expect_subscription_confirmed(page: Page) -> Locator:
    """
    Checkpoint: h1 ``Assinatura confirmada!`` and order line matching ``PAYMENT_PEDIDO_NUMERO_REGEX``.

    Returns the h1 locator for final assertions.
    """
    confirmed = page.get_by_role("heading", name="Assinatura confirmada!", level=1)
    expect(confirmed).to_be_visible()
    expect(page.get_by_text("Resumo do seu pedido", exact=True)).to_be_visible()
    expect(page.get_by_text(PAYMENT_PEDIDO_NUMERO_REGEX)).to_be_visible()
    return confirmed
