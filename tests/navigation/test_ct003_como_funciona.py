"""
CT003 — "Como Funciona" header navigation (docs/test-cases.md).

Objective:
    Verify the header link scrolls to the correct on-page section.

Stable locators (prefer ``get_by_role``):
    - Menu: role ``link``, accessible name ``Como Funciona``
    - Section title: role ``heading``, level 2, name ``Como Funciona?``

Assertions use short, stable visible text to reduce flake.
"""

from __future__ import annotations

import re

from playwright.sync_api import Page, expect
from utils.navigation import open_homepage

def test_ct003_como_funciona_header_navigates_to_how_it_works_section(page: Page):

    open_homepage(page)


    como_funciona = page.get_by_role("link", name="Como Funciona")
    expect(como_funciona).to_be_visible()
    como_funciona.click()

    expect(page).to_have_url(re.compile(r"#how-it-works"))

    section_heading = page.get_by_role("heading", name="Como Funciona?", level=2)
    expect(section_heading).to_be_visible()
    expect(section_heading).to_be_in_viewport()

    expect(page.get_by_text("Escolha seu plano", exact=True)).to_be_visible()
