"""
CT014 — Address autofill by CEP (docs/test-cases.md, address).

Objective:
    After a valid CEP and Search, street, neighborhood, city, and state are filled.

Preconditions:
    Delivery address section via ``go_to_address_step`` in ``utils/address_steps.py``.

Flow:
    Enter valid CEP → click ``Buscar`` → assert ``Rua``, ``Bairro``, ``Cidade``, ``Estado``.

Flake risks:
    - CEP API latency; ``lookup_address_by_cep`` uses an explicit timeout on the ``Rua`` field.
"""

from __future__ import annotations

from playwright.sync_api import Page, expect

from data.address_data import (
    ADDRESS_BAIRRO_ESPERADO,
    ADDRESS_CEP_VALIDO_AUTOCOMPLETE,
    ADDRESS_CIDADE_ESPERADA,
    ADDRESS_ESTADO_ESPERADO,
    ADDRESS_RUA_ESPERADA,
)
from utils.address_steps import lookup_address_by_cep, expect_delivery_address_heading, go_to_address_step
from utils.navigation import expect_subscribe_url


def test_ct014_cep_lookup_fills_street_neighborhood_city_state(page: Page):
    go_to_address_step(page)
    delivery_address_heading = expect_delivery_address_heading(page)

    lookup_address_by_cep(page, ADDRESS_CEP_VALIDO_AUTOCOMPLETE)

    expect(page.get_by_label("CEP")).to_have_value(ADDRESS_CEP_VALIDO_AUTOCOMPLETE)
    expect(page.get_by_label("Rua")).to_have_value(ADDRESS_RUA_ESPERADA)
    expect(page.get_by_label("Bairro")).to_have_value(ADDRESS_BAIRRO_ESPERADO)
    expect(page.get_by_label("Cidade")).to_have_value(ADDRESS_CIDADE_ESPERADA)
    expect(page.get_by_label("Estado")).to_have_value(ADDRESS_ESTADO_ESPERADO)

    expect(delivery_address_heading).to_be_visible()
    expect_subscribe_url(page)