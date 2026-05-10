"""
Steps up to the Payment step on ``/subscribe``.

Uses ``go_to_address_step`` (subscription → personal data → address) and ``complete_endereco_step``
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
from utils.address_steps import complete_endereco_step, go_to_address_step


def expect_pagamento_step(page: Page) -> Locator:
    """
    Checkpoint: payment step visible.

    Anchors on ``Resumo do Pedido`` + ``Finalizar Assinatura`` — the word ``Pagamento`` is duplicated
    (stepper + section title), so it is not used as the sole locator.
    """
    expect(page.get_by_text("Resumo do Pedido", exact=True)).to_be_visible()
    finalizar = page.get_by_role("button", name="Finalizar Assinatura")
    expect(finalizar).to_be_visible()
    return finalizar


def go_to_payment_step(page: Page) -> None:
    """Open subscribe flow through address (default data) until the payment form is shown."""
    go_to_address_step(page)
    complete_endereco_step(page)
    expect_pagamento_step(page)


def click_finalizar_assinatura(page: Page) -> None:
    """Click ``Finalizar Assinatura`` on the payment step."""
    finalizar = page.get_by_role("button", name="Finalizar Assinatura")
    expect(finalizar).to_be_visible()
    expect(finalizar).to_be_enabled()
    finalizar.click()


def fill_cartao(page: Page, *, numero: str) -> None:
    """Fill card form with default holder data; only ``numero`` varies by scenario."""
    page.get_by_label("Número do Cartão").fill(numero)
    page.get_by_label("Nome no Cartão").fill(PAYMENT_NOME_TITULAR)
    page.get_by_label("Validade").fill(PAYMENT_VALIDADE_FUTURA)
    page.get_by_label("CVV").fill(PAYMENT_CVV)
    page.get_by_label("CPF do Titular").fill(PAYMENT_CPF)


def expect_assinatura_confirmada(page: Page) -> Locator:
    """
    Checkpoint: h1 ``Assinatura confirmada!`` and order line matching ``PAYMENT_PEDIDO_NUMERO_REGEX``.

    Returns the h1 locator for final assertions.
    """
    confirmada = page.get_by_role("heading", name="Assinatura confirmada!", level=1)
    expect(confirmada).to_be_visible()
    expect(page.get_by_text("Resumo do seu pedido", exact=True)).to_be_visible()
    expect(page.get_by_text(PAYMENT_PEDIDO_NUMERO_REGEX)).to_be_visible()
    return confirmada
