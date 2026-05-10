"""
CT013 — Required or invalid CEP (docs/test-cases.md, address).

Objective:
    The user cannot continue with blank or malformed CEP.

Preconditions:
    Delivery address section via ``go_to_address_step`` in ``utils/address_steps.py``.

Scenarios:
    - Empty CEP: UI reuses ``CEP inválido.`` (same pattern as other Zod fields).
    - Malformed CEP (``ADDRESS_CEP_MALFORMED``): same message without calling the lookup API.

Flake risks:
    - Other address errors may show when CEP is empty; the test asserts the CEP message explicitly.
"""

from __future__ import annotations

from playwright.sync_api import Page, expect

from data.address_data import ADDRESS_CEP_MALFORMED, VALIDATION_MSG_CEP_INVALIDO
from utils.address_steps import expect_delivery_address_heading, go_to_address_step
from utils.navigation import expect_subscribe_url
from utils.subscription_steps import click_next


def test_ct013_empty_cep_blocks_progress(page: Page):
    go_to_address_step(page)
    delivery_address_heading = expect_delivery_address_heading(page)

    cep = page.get_by_label("CEP")
    expect(cep).to_be_visible()
    expect(cep).to_have_value("")

    click_next(page)

    expect(page.get_by_text(VALIDATION_MSG_CEP_INVALIDO, exact=True)).to_be_visible()
    expect(delivery_address_heading).to_be_visible()
    expect(cep).to_be_visible()
    expect_subscribe_url(page)


def test_ct013_malformed_cep_blocks_progress(page: Page):
    go_to_address_step(page)
    delivery_address_heading = expect_delivery_address_heading(page)

    cep = page.get_by_label("CEP")
    cep.fill(ADDRESS_CEP_MALFORMED)
    expect(cep).to_have_value(ADDRESS_CEP_MALFORMED)

    click_next(page)

    expect(page.get_by_text(VALIDATION_MSG_CEP_INVALIDO, exact=True)).to_be_visible()
    expect(delivery_address_heading).to_be_visible()
    expect(cep).to_be_visible()
    expect_subscribe_url(page)
