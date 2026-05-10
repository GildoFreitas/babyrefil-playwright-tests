"""
Steps to reach the ``Endereço de Entrega`` section on ``/subscribe``.

Reuses ``subscription_steps`` for banner → plan → monthly → personal data, then fills default
personal/baby fields so the CEP/address block is ready for tests.
"""

from __future__ import annotations

import re

from playwright.sync_api import Locator, Page, expect

from data.address_data import (
    ADDRESS_CEP_VALIDO_AUTOCOMPLETE,
    ADDRESS_COMPLEMENTO,
    ADDRESS_NUMERO,
)
from data.subscription_data import (
    SUBSCRIPTION_EMAIL,
    SUBSCRIPTION_IDADE_FAIXA_OPTION,
    SUBSCRIPTION_NOME_BEBE,
    SUBSCRIPTION_NOME_COMPLETO,
    SUBSCRIPTION_TELEFONE,
)
from utils.subscription_steps import (
    click_next,
    expect_personal_data_step,
    go_to_personal_data_step,
)


def expect_delivery_address_heading(page: Page) -> Locator:
    """Checkpoint: h3 ``Endereço de Entrega`` is visible."""
    heading = page.get_by_role("heading", name="Endereço de Entrega", level=3)
    expect(heading).to_be_visible()
    return heading


def go_to_address_step(page: Page) -> None:
    """
    Navigate to ``Seus Dados`` and fill personal + baby fields.

    The screen combines personal data, baby data, and delivery address on one page with a single
    ``Avançar`` that validates the whole form (Zod) and goes to Payment when valid. We therefore
    do **not** click ``Avançar`` here — the address block is already visible. Clicking ``Avançar``
    before the address is complete can flash transient address errors (cosmetic only).
    """
    go_to_personal_data_step(page)
    expect_personal_data_step(page)

    page.get_by_label("Nome Completo").fill(SUBSCRIPTION_NOME_COMPLETO)
    page.get_by_label("E-mail").fill(SUBSCRIPTION_EMAIL)
    page.get_by_label("Telefone").fill(SUBSCRIPTION_TELEFONE)
    page.get_by_label("Nome do Bebê").fill(SUBSCRIPTION_NOME_BEBE)

    page.get_by_label("Idade do Bebê").click()
    page.get_by_role("option", name=SUBSCRIPTION_IDADE_FAIXA_OPTION).click()

    expect_delivery_address_heading(page)


def lookup_address_by_cep(page: Page, cep: str) -> None:
    """Fill CEP, click ``Buscar``, wait until ``Rua`` has a non-empty value from the API."""
    page.get_by_label("CEP").fill(cep)
    buscar = page.get_by_role("button", name="Buscar")
    expect(buscar.first).to_be_visible()
    expect(buscar.first).to_be_enabled()
    buscar.first.click()
    rua = page.get_by_label("Rua")
    # Street may stay disabled after lookup; value from the API is enough.
    expect(rua).to_have_value(re.compile(r"\S"), timeout=20_000)


def complete_address_step(page: Page) -> None:
    """Complete address with default CEP lookup + number/complement, then click ``Avançar``."""
    lookup_address_by_cep(page, ADDRESS_CEP_VALIDO_AUTOCOMPLETE)
    page.get_by_label("Número").fill(ADDRESS_NUMERO)
    page.get_by_label("Complemento (Opcional)").fill(ADDRESS_COMPLEMENTO)
    click_next(page)
