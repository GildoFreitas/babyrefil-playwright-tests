"""
CT015 — Required address fields (docs/test-cases.md, address).

Objective:
    User cannot continue when mandatory address lines are empty after entering CEP.

Preconditions:
    Delivery address section via ``go_to_address_step`` in ``utils/address_steps.py``.

Data:
    Valid CEP filled; street, number, neighborhood, city, and state left empty (no ``Buscar``),
    aligned with the case table.

Flake risks:
    - Errors from other form blocks may appear; this test asserts all five address messages.
"""

from __future__ import annotations

from playwright.sync_api import Page, expect

from data.address_data import (
    ADDRESS_CEP_VALIDO_AUTOCOMPLETE,
    VALIDATION_MSG_BAIRRO_OBRIGATORIO,
    VALIDATION_MSG_CIDADE_OBRIGATORIA,
    VALIDATION_MSG_ENDERECO_OBRIGATORIO,
    VALIDATION_MSG_ESTADO_OBRIGATORIO,
    VALIDATION_MSG_NUMERO_OBRIGATORIO,
)
from utils.address_steps import expect_delivery_address_heading, go_to_address_step
from utils.navigation import expect_subscribe_url
from utils.subscription_steps import click_next


def test_ct015_valid_cep_without_other_fields_blocks_progress(page: Page):
    go_to_address_step(page)
    delivery_address_heading = expect_delivery_address_heading(page)

    cep = page.get_by_label("CEP")
    cep.fill(ADDRESS_CEP_VALIDO_AUTOCOMPLETE)
    expect(cep).to_have_value(ADDRESS_CEP_VALIDO_AUTOCOMPLETE)

    click_next(page)

    for msg in (
        VALIDATION_MSG_ENDERECO_OBRIGATORIO,
        VALIDATION_MSG_NUMERO_OBRIGATORIO,
        VALIDATION_MSG_BAIRRO_OBRIGATORIO,
        VALIDATION_MSG_CIDADE_OBRIGATORIA,
        VALIDATION_MSG_ESTADO_OBRIGATORIO,
    ):
        expect(page.get_by_text(msg, exact=True)).to_be_visible()

    expect(delivery_address_heading).to_be_visible()
    expect(cep).to_be_visible()
    expect_subscribe_url(page)
