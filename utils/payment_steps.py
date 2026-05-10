"""
Passos reutilizáveis até a etapa "Pagamento" no /subscribe.

Reutiliza `go_to_address_step` (subscription → dados pessoais → endereço) e completa o endereço
com a massa padrão (`complete_endereco_step`) para chegar à última etapa do fluxo.

Locators estáveis observados no código da aplicação (snapshot MCP):
- Etapa pagamento: "Resumo do Pedido" + botão "Finalizar Assinatura" (CTA único da etapa).
- Campos do cartão (labels): "Número do Cartão", "Nome no Cartão", "Validade", "CVV", "CPF do Titular".
"""

from __future__ import annotations

from playwright.sync_api import Locator, Page, expect

from utils.address_steps import complete_endereco_step, go_to_address_step


def expect_pagamento_step(page: Page) -> Locator:
    """
    Checkpoint: etapa "Pagamento" visível.

    Usa "Resumo do Pedido" (texto único da etapa) + botão "Finalizar Assinatura"
    como âncora estável — o texto "Pagamento" aparece duplicado (indicador de etapa
    e título da seção), por isso não é usado como locator único.
    """
    expect(page.get_by_text("Resumo do Pedido", exact=True)).to_be_visible()
    finalizar = page.get_by_role("button", name="Finalizar Assinatura")
    expect(finalizar).to_be_visible()
    return finalizar


def go_to_payment_step(page: Page) -> None:
    """
    Abre /subscribe, percorre Plano → Recorrência → Dados Pessoais → Endereço (massa padrão)
    e clica em Avançar até exibir o formulário de pagamento.
    """
    go_to_address_step(page)
    complete_endereco_step(page)
    expect_pagamento_step(page)


def click_finalizar_assinatura(page: Page) -> None:
    """Clica no CTA "Finalizar Assinatura" da etapa de pagamento (auto-retry via expect)."""
    finalizar = page.get_by_role("button", name="Finalizar Assinatura")
    expect(finalizar).to_be_visible()
    expect(finalizar).to_be_enabled()
    finalizar.click()
