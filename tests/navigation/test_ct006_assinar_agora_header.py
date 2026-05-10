"""
CT006 — Header "Assinar Agora" CTA (docs/test-cases.md).

MCP / a11y exploration:
    - Header: ``banner`` → link ``Assinar Agora`` → ``/subscribe`` (restrict to ``banner`` so the hero CTA is not clicked by mistake).
    - Subscribe flow: ``main`` shows step ``1`` / ``Plano``; h2 ``Escolha o seu plano``.
    - Plans: ``Plano Essencial``, ``Plano Conforto``, ``Plano Completo``; buttons
      ``Selecionar Plano`` or ``Plano Selecionado`` depending on default selection.

Flake risks:
    - Default selected plan can change button labels; do not bind to one plan — assert all three
      names and the step title.

Dynamic content:
    - Prices and benefit lists can change; do not use them as primary assertions.
"""

from __future__ import annotations

from playwright.sync_api import Page, expect

from utils.navigation import expect_subscribe_url, open_homepage

_HEADER_SUBSCRIBE_LINK = "Assinar Agora"

def test_ct006_header_assinar_agora_opens_subscribe_plan_step(page: Page):
    open_homepage(page)

    banner = page.get_by_role("banner")
    header_cta = banner.get_by_role("link", name=_HEADER_SUBSCRIBE_LINK, exact=True)
    expect(header_cta).to_be_visible()
    expect(header_cta).to_be_enabled()

    header_cta.click()
    expect_subscribe_url(page)

    expect(page.get_by_role("main")).to_be_visible()
    plan_heading = page.get_by_role("heading", name="Escolha o seu plano", level=2)
    expect(plan_heading).to_be_visible()
    expect(plan_heading).to_be_in_viewport()

    expect(page.get_by_text("Plano Essencial", exact=True)).to_be_visible()
    expect(page.get_by_text("Plano Conforto", exact=True)).to_be_visible()
    expect(page.get_by_text("Plano Completo", exact=True)).to_be_visible()
