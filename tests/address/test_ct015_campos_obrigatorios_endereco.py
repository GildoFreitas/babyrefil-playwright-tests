"""
CT015 — Validar campos obrigatórios do endereço (test-cases.md).

Pré-condições: etapa "Endereço de Entrega" via `go_to_address_step` em utils/address_steps.py.

Massa: CEP válido preenchido; rua, número, bairro, cidade e estado permanecem vazios (sem acionar
"Buscar", alinhado à tabela do caso — somente o CEP informado).

Riscos de flake:
- Mensagens de outros blocos do formulário; o teste valida as cinco cópias do endereço.
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
from utils.address_steps import expect_endereco_entrega_step, go_to_address_step
from utils.navigation import expect_subscribe_url
from utils.subscription_steps import click_avancar


def test_ct015_cep_sem_buscar_e_demais_vazios_impede_avanco_e_exibe_erros(page: Page):
    go_to_address_step(page)
    endereco = expect_endereco_entrega_step(page)

    cep = page.get_by_label("CEP")
    cep.fill(ADDRESS_CEP_VALIDO_AUTOCOMPLETE)
    expect(cep).to_have_value(ADDRESS_CEP_VALIDO_AUTOCOMPLETE)

    click_avancar(page)

    for msg in (
        VALIDATION_MSG_ENDERECO_OBRIGATORIO,
        VALIDATION_MSG_NUMERO_OBRIGATORIO,
        VALIDATION_MSG_BAIRRO_OBRIGATORIO,
        VALIDATION_MSG_CIDADE_OBRIGATORIA,
        VALIDATION_MSG_ESTADO_OBRIGATORIO,
    ):
        expect(page.get_by_text(msg, exact=True)).to_be_visible()

    expect(endereco).to_be_visible()
    expect(cep).to_be_visible()
    expect_subscribe_url(page)
