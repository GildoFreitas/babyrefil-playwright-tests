"""
CT008 — Validar campo "Nome Completo" obrigatório (test-cases.md).

Pré-condições: `go_to_personal_data_step` em utils/subscription_steps.py.

Riscos de flake:
- Combobox de idade: fechar após escolher a option antes de Avançar.
- Radio Mensal sr-only: tratado em subscription_steps.select_frequencia_mensal.
"""

from __future__ import annotations

import re

from playwright.sync_api import Page, expect

from data.subscription_data import (
    SUBSCRIPTION_EMAIL,
    SUBSCRIPTION_IDADE_FAIXA_OPTION,
    SUBSCRIPTION_NOME_BEBE,
    SUBSCRIPTION_TELEFONE,
    VALIDATION_MSG_NOME_COMPLETO_OBRIGATORIO,
)
from utils.env import get_base_url
from utils.subscription_steps import click_avancar, go_to_personal_data_step


def test_ct008_nome_completo_vazio_impede_avanco_e_exibe_erro(page: Page):
    base = get_base_url()

    go_to_personal_data_step(page)

    expect(page.get_by_text("Seus Dados", exact=True)).to_be_visible()
    dados_pessoais = page.get_by_role("heading", name="Dados Pessoais", level=3)
    expect(dados_pessoais).to_be_visible()

    nome_completo = page.get_by_label("Nome Completo")

    page.get_by_label("E-mail").fill(SUBSCRIPTION_EMAIL)
    page.get_by_label("Telefone").fill(SUBSCRIPTION_TELEFONE)
    page.get_by_label("Nome do Bebê").fill(SUBSCRIPTION_NOME_BEBE)

    page.get_by_label("Idade do Bebê").click()
    page.get_by_role("option", name=SUBSCRIPTION_IDADE_FAIXA_OPTION).click()

    expect(nome_completo).to_be_visible()
    expect(nome_completo).to_have_value("")

    click_avancar(page)

    expect(page.get_by_text(VALIDATION_MSG_NOME_COMPLETO_OBRIGATORIO, exact=True)).to_be_visible()
    expect(dados_pessoais).to_be_visible()
    expect(nome_completo).to_be_visible()
    expect(page).to_have_url(re.compile(re.escape(base) + r"/subscribe/?$"))
