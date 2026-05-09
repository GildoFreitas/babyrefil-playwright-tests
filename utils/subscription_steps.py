"""
Passos reutilizáveis do fluxo de assinatura (exploração + bundle Next.js da página /subscribe).

Locators estáveis observados no código da aplicação:
- CTA header: link "Assinar Agora" no banner.
- Plano: heading "Escolha o seu plano"; botões "Selecionar Plano" / "Plano Selecionado".
- Avanço entre etapas: botão com texto "Avançar" (presente no bundle; deve aparecer após seleção de plano).
- Recorrência: opções com texto "Mensal" / "Quinzenal" (cards clicáveis).
- Dados: heading "Dados Pessoais"; labels "Nome Completo", "E-mail", "Telefone", "Nome do Bebê", "Idade do Bebê".
"""

from __future__ import annotations

import re

from playwright.sync_api import Page, expect

from utils.env import get_base_url
from utils.navigation import open_homepage


def open_subscribe_from_banner(page: Page) -> None:
    """Home (via open_homepage) → /subscribe pelo link do header."""
    open_homepage(page)
    cta = page.get_by_role("banner").get_by_role("link", name="Assinar Agora")
    expect(cta).to_be_visible()
    expect(cta).to_be_enabled()
    cta.click()
    base = get_base_url()
    expect(page).to_have_url(re.compile(re.escape(base) + r"/subscribe/?$"))


def ensure_plan_selected(page: Page) -> None:
    """Confirma plano e avança para recorrência (UI: clicar em Plano Selecionado ou Selecionar Plano)."""
    expect(page.get_by_role("heading", name="Escolha o seu plano", level=2)).to_be_visible()
    plano_sel = page.get_by_role("button", name="Plano Selecionado")
    if plano_sel.count() > 0:
        plano_sel.click()
        return
    selecionar = page.get_by_role("button", name="Selecionar Plano")
    expect(selecionar.first).to_be_visible()
    selecionar.first.click()


def click_avancar(page: Page) -> None:
    """Clica no botão Avançar da etapa atual (auto-retry via expect)."""
    avancar = page.get_by_role("button", name=re.compile(r"^\s*Avançar\s*$", re.I))
    expect(avancar.first).to_be_visible()
    expect(avancar.first).to_be_enabled()
    avancar.first.click()


def select_frequencia_mensal(page: Page) -> None:
    """Seleciona recorrência Mensal (clique na linha do card; o radio é sr-only)."""
    mensal = page.get_by_role("radio", name="Mensal A cada 30 dias")
    expect(mensal).to_be_visible()
    page.get_by_role("radiogroup").get_by_text("Mensal", exact=True).click()


def expect_dados_pessoais_step(page: Page) -> None:
    """Checkpoint: etapa de dados pessoais visível."""
    expect(page.get_by_role("heading", name="Dados Pessoais", level=3)).to_be_visible()


def go_to_personal_data_step(page: Page) -> None:
    """
    Abre /subscribe e avança: Plano → Recorrência (Mensal) → Dados Pessoais.
    """
    open_subscribe_from_banner(page)
    ensure_plan_selected(page)
    expect(page.get_by_text("Frequência da Entrega", exact=True)).to_be_visible()
    select_frequencia_mensal(page)
    click_avancar(page)
    expect_dados_pessoais_step(page)
