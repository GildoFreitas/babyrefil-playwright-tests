"""
CT014 — Validar preenchimento automático de endereço pelo CEP (test-cases.md).

Pré-condições: etapa "Endereço de Entrega" via `go_to_address_step` em utils/address_steps.py.

Fluxo: informar CEP válido → Buscar → validar rua, bairro, cidade e estado.

Riscos de flake:
- Latência da API de CEP; `buscar_endereco_por_cep` usa timeout explícito no campo Rua.
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
from utils.address_steps import buscar_endereco_por_cep, expect_endereco_entrega_step, go_to_address_step
from utils.navigation import expect_subscribe_url


def test_ct014_buscar_cep_preenche_rua_bairro_cidade_estado(page: Page):
    go_to_address_step(page)
    endereco = expect_endereco_entrega_step(page)

    buscar_endereco_por_cep(page, ADDRESS_CEP_VALIDO_AUTOCOMPLETE)

    expect(page.get_by_label("CEP")).to_have_value(ADDRESS_CEP_VALIDO_AUTOCOMPLETE)
    expect(page.get_by_label("Rua")).to_have_value(ADDRESS_RUA_ESPERADA)
    expect(page.get_by_label("Bairro")).to_have_value(ADDRESS_BAIRRO_ESPERADO)
    expect(page.get_by_label("Cidade")).to_have_value(ADDRESS_CIDADE_ESPERADA)
    expect(page.get_by_label("Estado")).to_have_value(ADDRESS_ESTADO_ESPERADO)

    expect(endereco).to_be_visible()
    expect_subscribe_url(page)
