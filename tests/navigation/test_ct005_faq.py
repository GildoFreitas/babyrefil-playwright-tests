"""
CT005 — "FAQ" header navigation (docs/test-cases.md).

MCP / a11y exploration:
    - Menu: role ``link``, name ``FAQ``, target ``/#faq``.
    - After click: URL fragment ``#faq``.
    - Section: level-2 heading ``Perguntas Frequentes``; introductory paragraph in the FAQ block.
    - Accordion: question buttons; expanding reveals a ``region`` with the same accessible name
      and answer text inside.

Flake risks:
    - Collapsed answers may be absent from the a11y tree until expanded; the test opens one item
      and asserts on the region plus a short answer substring.
    - Other buttons on the page have distinct names from FAQ items.

Dynamic content:
    - Long answer copy may change; keep only a short stable substring for assertions.
"""

from __future__ import annotations

import re

from playwright.sync_api import Page, expect
from utils.navigation import open_homepage

_FAQ_QUESTION_BUTTONS = (
    "Como funciona o clube de assinatura?",
    "Posso alterar meu plano ou a frequência?",
    "Quais são as formas de pagamento?",
    "Como funciona a entrega?",
    "E se eu quiser cancelar?",
)

def test_ct005_faq_header_navigates_to_faq_section(page: Page):

    open_homepage(page)

    faq_link = page.get_by_role("link", name="FAQ", exact=True)
    expect(faq_link).to_be_visible()
    expect(faq_link).to_be_enabled()

    faq_link.click()
    expect(page).to_have_url(re.compile(r"#faq"))

    section_title = page.get_by_role("heading", name="Perguntas Frequentes", level=2)
    expect(section_title).to_be_visible()
    expect(section_title).to_be_in_viewport()

    for question in _FAQ_QUESTION_BUTTONS:
        expect(page.get_by_role("button", name=question)).to_be_visible()

    first = _FAQ_QUESTION_BUTTONS[0]
    page.get_by_role("button", name=first).click()

    answer_region = page.get_by_role("region", name=first)
    expect(answer_region).to_be_visible()
    expect(answer_region.get_by_text("Você escolhe um de nossos planos", exact=False)).to_be_visible()
