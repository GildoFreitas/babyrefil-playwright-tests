"""
CT004 — Validar navegação do botão "Planos" (test-cases.md).

Exploração MCP (snapshot de acessibilidade):
- Menu: role "link", nome exato "Planos" (href /#plans) — usar exact=True para não
  acionar o link "Ver Planos" do hero.
- Após o clique: URL com fragmento #plans.
- Seção: heading nível 2 "Planos para todos os momentos".
- Planos exibidos (texto visível estável): "Plano Essencial", "Plano Conforto",
  "Plano Completo" (atende passo 3 do CT004).

Riscos de flake:
- Conteúdo abaixo da dobra depende de scroll; heading + planos com expect + viewport
  no título da seção reduz falso negativo.
- Preços (R$ 119,90 etc.) podem mudar; não acoplar asserções a valores monetários.

Elementos dinâmicos:
- Nenhum identificado na seção de planos além de copy estável dos nomes dos planos.
"""

from __future__ import annotations

import os
import re

from dotenv import load_dotenv
from playwright.sync_api import Page, expect

load_dotenv()


def _base_url() -> str:
    """URL base a partir do .env; falha cedo se ausente."""
    url = (os.getenv("BASE_URL") or "").strip().rstrip("/")
    if not url:
        raise RuntimeError(
            "Defina BASE_URL no arquivo .env (ex.: BASE_URL=https://babyrefil.vercel.app)"
        )
    return url


def test_ct004_planos_header_navigates_to_plans_section(page: Page):
    """
    Fluxo independente: home → clique em "Planos" no header → âncora #plans →
    valida título da seção e os três planos (Essencial, Conforto, Completo).
    """
    base = _base_url()

    # Checkpoint: homepage carregada; URL coerente com BASE_URL antes do menu
    page.goto(base)
    expect(page).to_have_url(re.compile(re.escape(base) + r"/?$"))

    # Garante que o alvo do clique existe e está acessível (interação dependente)
    planos_nav = page.get_by_role("link", name="Planos", exact=True)
    expect(planos_nav).to_be_visible()
    expect(planos_nav).to_be_enabled()

    # Ação crítica: navegação para a seção de planos
    planos_nav.click()

    # Checkpoint: fragmento da seção de planos
    expect(page).to_have_url(re.compile(r"#plans"))

    # Checkpoint: título da seção visível e rolado para a viewport
    section_title = page.get_by_role(
        "heading", name="Planos para todos os momentos", level=2
    )
    expect(section_title).to_be_visible()
    expect(section_title).to_be_in_viewport()

    # Passo 3 CT004: planos Essencial, Conforto e Completo (nomes como na UI)
    expect(page.get_by_text("Plano Essencial", exact=True)).to_be_visible()
    expect(page.get_by_text("Plano Conforto", exact=True)).to_be_visible()
    expect(page.get_by_text("Plano Completo", exact=True)).to_be_visible()
