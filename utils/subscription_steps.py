"""
Reusable steps for the subscription flow (MCP exploration + Next.js bundle for ``/subscribe``).

Stable locators observed in the app:
    - Header CTA: ``banner`` → link ``Assinar Agora``.
    - Plan step: h2 ``Escolha o seu plano``; buttons ``Selecionar Plano`` / ``Plano Selecionado``.
    - Step navigation: button text ``Avançar`` (present in bundle; visible after plan selection).
    - Recurrence: options ``Mensal`` / ``Quinzenal`` (clickable cards; radio may be sr-only).
    - Data step: text ``Seus Dados``; h3 ``Dados Pessoais``; form labels as in the UI.
"""

from __future__ import annotations

import re

from playwright.sync_api import Locator, Page, expect

from utils.navigation import expect_subscribe_url, open_homepage


def open_subscribe_from_banner(page: Page) -> None:
    """Open home (``open_homepage``) then go to ``/subscribe`` via the header link."""
    open_homepage(page)
    cta = page.get_by_role("banner").get_by_role("link", name="Assinar Agora")
    expect(cta).to_be_visible()
    expect(cta).to_be_enabled()
    cta.click()
    expect_subscribe_url(page)


def ensure_plan_selected(page: Page) -> None:
    """Ensure a plan is selected (``Plano Selecionado`` or click ``Selecionar Plano``)."""
    expect(page.get_by_role("heading", name="Escolha o seu plano", level=2)).to_be_visible()
    plano_sel = page.get_by_role("button", name="Plano Selecionado")
    if plano_sel.count() > 0:
        plano_sel.click()
        return
    selecionar = page.get_by_role("button", name="Selecionar Plano")
    expect(selecionar.first).to_be_visible()
    selecionar.first.click()


def click_avancar(page: Page) -> None:
    """Click the ``Avançar`` button on the current step (auto-retry via ``expect``)."""
    avancar = page.get_by_role("button", name=re.compile(r"^\s*Avançar\s*$", re.I))
    expect(avancar.first).to_be_visible()
    expect(avancar.first).to_be_enabled()
    avancar.first.click()


def select_frequencia_mensal(page: Page) -> None:
    """Select monthly recurrence by clicking the card row (radio may be sr-only)."""
    mensal = page.get_by_role("radio", name="Mensal A cada 30 dias")
    expect(mensal).to_be_visible()
    page.get_by_role("radiogroup").get_by_text("Mensal", exact=True).click()


def expect_dados_pessoais_step(page: Page) -> Locator:
    """
    Checkpoint: ``Seus Dados`` visible with h3 ``Dados Pessoais``.

    Returns the h3 locator for reuse in assertions.
    """
    expect(page.get_by_text("Seus Dados", exact=True)).to_be_visible()
    dados_pessoais = page.get_by_role("heading", name="Dados Pessoais", level=3)
    expect(dados_pessoais).to_be_visible()
    return dados_pessoais


def go_to_personal_data_step(page: Page) -> None:
    """
    Open ``/subscribe`` and advance: Plan → Recurrence (monthly) → click ``Avançar`` to the form.

    After this, call ``expect_dados_pessoais_step(page)`` to validate and obtain the section locator.
    """
    open_subscribe_from_banner(page)
    ensure_plan_selected(page)
    expect(page.get_by_text("Frequência da Entrega", exact=True)).to_be_visible()
    select_frequencia_mensal(page)
    click_avancar(page)
