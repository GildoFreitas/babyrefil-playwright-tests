"""
CT007 — "Assinar agora" in the plans section (docs/test-cases.md).

MCP exploration:
    - Step 2: ``link`` ``Planos`` (``exact=True``) → ``/#plans``; h2 ``Planos para todos os momentos``.
    - Step 3: inside ``main``, ``link`` ``Assinar agora`` (lowercase "agora", ``/subscribe``) —
      distinct from the hero ``Assinar Agora``.
    - After click: ``/subscribe`` with h2 ``Escolha o seu plano`` and stepper labels including ``Recorrência``.

Step 4 (recurrence):
    In the current UI there is no separate "Continue" control that moves from plan-only to a
    recurrence-only screen before personal data; the test asserts that ``Recorrência`` appears
    in the stepper alongside the plan step, showing the wizard includes that stage.

Flake risks:
    - ``#plans`` layout and section CTA depend on layout; ``expect`` auto-retry covers load timing.

Dynamic content:
    - Default plan on ``/subscribe`` may vary; do not assert a specific pre-selected plan.
"""

from __future__ import annotations

import re

from playwright.sync_api import Page, expect
from utils.navigation import expect_subscribe_url, open_homepage

_PLANS_SECTION_CTA = "Assinar agora"

def test_ct007_planos_section_assinar_agora_opens_subscribe_flow(page: Page):
    open_homepage(page)

    planos_menu = page.get_by_role("link", name="Planos", exact=True)
    expect(planos_menu).to_be_visible()
    planos_menu.click()
    expect(page).to_have_url(re.compile(r"#plans"))

    plans_heading = page.get_by_role("heading", name="Planos para todos os momentos", level=2)
    expect(plans_heading).to_be_visible()
    expect(plans_heading).to_be_in_viewport()

    main = page.get_by_role("main")
    plans_cta = main.get_by_role("link", name=_PLANS_SECTION_CTA, exact=True)
    expect(plans_cta).to_be_visible()
    expect(plans_cta).to_be_enabled()
    plans_cta.click()

    expect_subscribe_url(page)

    expect(page.get_by_role("main")).to_be_visible()
    plan_step_heading = page.get_by_role("heading", name="Escolha o seu plano", level=2)
    expect(plan_step_heading).to_be_visible()
    expect(plan_step_heading).to_be_in_viewport()

    expect(page.get_by_role("main").get_by_text("Recorrência", exact=True)).to_be_visible()
