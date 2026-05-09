"""
CT005 — Validar navegação do botão "FAQ" (test-cases.md).

Exploração MCP (snapshot de acessibilidade):
- Menu: role "link", nome "FAQ", destino /#faq.
- Após o clique: URL com fragmento #faq.
- Seção: heading nível 2 "Perguntas Frequentes"; parágrafo introdutório da área FAQ.
- Itens do acordeão: role "button" com o texto da pergunta; ao expandir, role "region"
  com o mesmo nome acessível da pergunta e texto de resposta no interior.

Riscos de flake:
- Acordeão: respostas fechadas não aparecem no DOM até expandir; o teste abre um item
  e valida região + trecho curto da resposta (evita parágrafo inteiro frágil).
- Outros botões na página têm nomes distintos dos itens do FAQ.

Elementos dinâmicos:
- Copy longo das respostas pode mudar; manter apenas substring estável e curta.
"""

from __future__ import annotations

import os
import re

from dotenv import load_dotenv
from playwright.sync_api import Page, expect

load_dotenv()

# Perguntas observadas no snapshot MCP (todas visíveis na seção sem expandir).
_FAQ_QUESTION_BUTTONS = (
    "Como funciona o clube de assinatura?",
    "Posso alterar meu plano ou a frequência?",
    "Quais são as formas de pagamento?",
    "Como funciona a entrega?",
    "E se eu quiser cancelar?",
)


def _base_url() -> str:
    """URL base a partir do .env; falha cedo se ausente."""
    url = (os.getenv("BASE_URL") or "").strip().rstrip("/")
    if not url:
        raise RuntimeError(
            "Defina BASE_URL no arquivo .env (ex.: BASE_URL=https://babyrefil.vercel.app)"
        )
    return url


def test_ct005_faq_header_navigates_to_faq_section(page: Page):
    """
    Fluxo independente: home → FAQ no header → #faq → perguntas visíveis →
    expande um item → região e resposta visíveis (passo 3 do CT005).
    """
    base = _base_url()

    # Checkpoint: homepage carregada
    page.goto(base)
    expect(page).to_have_url(re.compile(re.escape(base) + r"/?$"))

    faq_link = page.get_by_role("link", name="FAQ", exact=True)
    expect(faq_link).to_be_visible()
    expect(faq_link).to_be_enabled()

    # Ação crítica: âncora da seção FAQ
    faq_link.click()
    expect(page).to_have_url(re.compile(r"#faq"))

    # Checkpoint: título da seção na viewport
    section_title = page.get_by_role("heading", name="Perguntas Frequentes", level=2)
    expect(section_title).to_be_visible()
    expect(section_title).to_be_in_viewport()

    # Passo 3: perguntas exibidas (botões do acordeão com nome acessível único)
    for question in _FAQ_QUESTION_BUTTONS:
        expect(page.get_by_role("button", name=question)).to_be_visible()

    # Conteúdo de resposta: expande o primeiro item e valida region + trecho da resposta
    first = _FAQ_QUESTION_BUTTONS[0]
    page.get_by_role("button", name=first).click()

    answer_region = page.get_by_role("region", name=first)
    expect(answer_region).to_be_visible()
    # Trecho curto observado no MCP (menos sujeito a mudanças de copy longo)
    expect(answer_region.get_by_text("Você escolhe um de nossos planos", exact=False)).to_be_visible()
