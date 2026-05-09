"""
CT006 — Validar botão "Assine Agora" do header (test-cases.md).

Nota de alinhamento com a UI: o caso fala em "Assine Agora"; o nome acessível
no banner é "Assinar Agora" (link para /subscribe). O teste usa o texto real e
restringe ao `banner` para não clicar no "Assinar Agora" do hero.

Exploração MCP (snapshot de acessibilidade):
- Header: `banner` → `link "Assinar Agora"` → `/subscribe`.
- Fluxo de assinatura: `main` com passo "1" / "Plano"; heading h2 "Escolha o seu plano".
- Planos na etapa 1: textos "Plano Essencial", "Plano Conforto", "Plano Completo";
  botões "Selecionar Plano" ou estado "Plano Selecionado" conforme plano default.

Riscos de flake:
- Plano pré-selecionado pode mudar o rótulo de um dos botões; não acoplar a um
  plano específico — apenas nomes dos três planos + título da etapa.

Elementos dinâmicos:
- Preços e lista de benefícios podem mudar; não usar como asserção principal.
"""

from __future__ import annotations

from playwright.sync_api import Page, expect

from utils.navigation import expect_subscribe_url, open_homepage

_HEADER_SUBSCRIBE_LINK = "Assinar Agora"

def test_ct006_header_assinar_agora_opens_subscribe_plan_step(page: Page):
    """
    Fluxo independente: home → link "Assinar Agora" apenas no banner → /subscribe →
    tela de escolha de plano com os três planos visíveis.
    """
    # Checkpoint: homepage
    open_homepage(page)

    # Alvo exclusivo do header (evita CTA duplicado no hero)
    banner = page.get_by_role("banner")
    header_cta = banner.get_by_role("link", name=_HEADER_SUBSCRIBE_LINK, exact=True)
    expect(header_cta).to_be_visible()
    expect(header_cta).to_be_enabled()

    # Ação crítica: início do fluxo de assinatura
    header_cta.click()
    expect_subscribe_url(page)

    # Checkpoint: etapa de plano no fluxo (título da etapa — estável no MCP)
    expect(page.get_by_role("main")).to_be_visible()
    plan_heading = page.get_by_role("heading", name="Escolha o seu plano", level=2)
    expect(plan_heading).to_be_visible()
    expect(plan_heading).to_be_in_viewport()

    # Passo 3 CT006: planos exibidos na seleção
    expect(page.get_by_text("Plano Essencial", exact=True)).to_be_visible()
    expect(page.get_by_text("Plano Conforto", exact=True)).to_be_visible()
    expect(page.get_by_text("Plano Completo", exact=True)).to_be_visible()
