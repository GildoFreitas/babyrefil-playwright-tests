"""
CT004 — "Planos" header navigation (docs/test-cases.md).

MCP / a11y exploration:
    - Menu: role ``link``, exact name ``Planos`` (``/#plans``) — ``exact=True`` avoids the hero
      ``Ver Planos`` link.
    - After click: URL fragment ``#plans``.
    - Section: level-2 heading ``Planos para todos os momentos``.
    - Plans (stable visible text): ``Plano Essencial``, ``Plano Conforto``, ``Plano Completo``.

Flake risks:
    - Below-the-fold content depends on scroll; heading + ``to_be_in_viewport`` on the section title
      reduces false negatives.
    - Do not assert monetary amounts (e.g. R$ 119,90); copy can change.

Dynamic content:
    - No notable dynamic elements in the plans section beyond stable plan names.
"""

from __future__ import annotations

import re

from playwright.sync_api import Page, expect
from utils.navigation import open_homepage

def test_ct004_plans_header_navigation(page: Page):

    open_homepage(page)

    plans_nav = page.get_by_role("link", name="Planos", exact=True)
    expect(plans_nav).to_be_visible()
    expect(plans_nav).to_be_enabled()

    plans_nav.click()

    expect(page).to_have_url(re.compile(r"#plans"))

    section_title = page.get_by_role(
        "heading", name="Planos para todos os momentos", level=2
    )
    expect(section_title).to_be_visible()
    expect(section_title).to_be_in_viewport()

    expect(page.get_by_text("Plano Essencial", exact=True)).to_be_visible()
    expect(page.get_by_text("Plano Conforto", exact=True)).to_be_visible()
    expect(page.get_by_text("Plano Completo", exact=True)).to_be_visible()
