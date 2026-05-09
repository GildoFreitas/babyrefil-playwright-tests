"""
CT007 — Validar botão "Assine Agora" da seção de planos (test-cases.md).

Exploração MCP:
- Passo 2: `link "Planos"` (exact=True) leva a `/#plans`; heading h2 "Planos para todos os momentos".
- Passo 3: em `main`, `link "Assinar agora"` (nome com 'a' minúsculo em "agora", href /subscribe)
  distinto do hero `link "Assinar Agora"`.
- Pós-clique: `/subscribe` com heading "Escolha o seu plano" e stepper com rótulos "Plano",
  "Recorrência", etc.

Passo 4 (recorrência): no ambiente atual não há controle visível (ex.: "Continuar") que
leve do passo 1 ao formulário exclusivo da recorrência; o teste valida que o fluxo de
assinatura exibe a etapa "Recorrência" no stepper junto à tela de seleção de plano,
como indicador de que o wizard inclui essa etapa.

Riscos de flake:
- Âncora #plans e CTA da seção dependem de layout; `expect` com auto-retry cobre carregamento.

Elementos dinâmicos:
- Plano pré-selecionado no /subscribe pode variar; não acoplar a um plano específico.
"""

from __future__ import annotations

import re

from playwright.sync_api import Page, expect
from utils.navigation import expect_subscribe_url, open_homepage

_PLANS_SECTION_CTA = "Assinar agora"

def test_ct007_planos_section_assinar_agora_opens_subscribe_flow(page: Page):
    """
    Home → seção Planos (nav) → CTA da seção de planos → /subscribe →
    planos + indicador da etapa Recorrência no fluxo.
    """
    # Checkpoint: homepage
    open_homepage(page)

    # Passo 2: navegar até a seção de planos (menu superior)
    planos_menu = page.get_by_role("link", name="Planos", exact=True)
    expect(planos_menu).to_be_visible()
    planos_menu.click()
    expect(page).to_have_url(re.compile(r"#plans"))

    plans_heading = page.get_by_role("heading", name="Planos para todos os momentos", level=2)
    expect(plans_heading).to_be_visible()
    expect(plans_heading).to_be_in_viewport()

    # Passo 3: CTA da seção de planos (não confundir com "Assinar Agora" do hero)
    main = page.get_by_role("main")
    plans_cta = main.get_by_role("link", name=_PLANS_SECTION_CTA, exact=True)
    expect(plans_cta).to_be_visible()
    expect(plans_cta).to_be_enabled()
    plans_cta.click()

    expect_subscribe_url(page)

    # Fluxo de assinatura: etapa de seleção de plano carregada
    expect(page.get_by_role("main")).to_be_visible()
    plan_step_heading = page.get_by_role("heading", name="Escolha o seu plano", level=2)
    expect(plan_step_heading).to_be_visible()
    expect(plan_step_heading).to_be_in_viewport()

    # Passo 4: presença da etapa "Recorrência" no stepper do wizard (estrutura do fluxo)
    expect(page.get_by_role("main").get_by_text("Recorrência", exact=True)).to_be_visible()
