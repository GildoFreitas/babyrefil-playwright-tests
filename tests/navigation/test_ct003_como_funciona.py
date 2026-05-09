"""
CT003 — Validar navegação do botão "Como Funciona" (test-cases.md).

Locators estáveis (preferência por get_by_role):
- Link do menu: role "link", nome "Como Funciona"
- Título da seção: role "heading", nível 2, nome "Como Funciona?"

Validações enxutas (menos dependência de textos longos = menos flake).
"""

from __future__ import annotations

import re

from playwright.sync_api import Page, expect
from utils.navigation import open_homepage

def test_ct003_como_funciona_header_navigates_to_how_it_works_section(page: Page):
    """
    Fluxo: home → clique em "Como Funciona" → âncora #how-it-works → asserções mínimas.
    Não depende de outros testes; estado vem só do goto + interação deste caso.
    """

    # Checkpoint: página inicial acessível antes de interagir com o menu
    open_homepage(page)


    # Ação crítica: navegação interna por âncora (mesma página, hash muda)
    como_funciona = page.get_by_role("link", name="Como Funciona")
    expect(como_funciona).to_be_visible()
    como_funciona.click()

    # Essencial: URL com fragmento esperado após o clique
    expect(page).to_have_url(re.compile(r"#how-it-works"))

    # Essencial: heading da seção visível e na viewport (confirma scroll da âncora)
    section_heading = page.get_by_role("heading", name="Como Funciona?", level=2)
    expect(section_heading).to_be_visible()
    expect(section_heading).to_be_in_viewport()

    # Essencial: um elemento representativo curto da seção (primeiro passo), sem parágrafos longos
    expect(page.get_by_text("Escolha seu plano", exact=True)).to_be_visible()
