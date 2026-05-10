"""
CT001 — Adesão de Assinatura com Sucesso (test-cases.md, Fluxo de Assinatura).

Pré-condições: etapa "Pagamento" via `go_to_payment_step` em utils/payment_steps.py
(percorre Plano → Recorrência → Dados Pessoais → Endereço com a massa padrão).

Cenário: cartão Visa válido (`PAYMENT_CARD_VISA_VALIDO`) → pagamento aprovado e tela de confirmação
exibida com:
- Heading h1 "Assinatura confirmada!"
- "Resumo do seu pedido" + número do pedido no formato `BR<13 dígitos>` (`PAYMENT_PEDIDO_NUMERO_REGEX`)
- Cabeçalhos do resumo: "Plano", "Frequência", "Endereço de Entrega", "Próxima Entrega"
- Data estimada de entrega no padrão pt-BR (`PAYMENT_DATA_ENTREGA_REGEX`)

Nota de alinhamento com a UI: o caso fala em "Confirmar Pagamento"; o CTA real é "Finalizar Assinatura".
A confirmação acontece in-place (mesma URL `/subscribe`), não há redirect — validamos pelo conteúdo da tela.

Riscos de flake:
- Número do pedido é dinâmico (timestamp); validamos por regex de formato, não por valor exato.
- Data por extenso varia diariamente; validamos por padrão "<dia> de <mês> de <ano>".
"""

from __future__ import annotations

from playwright.sync_api import Page, expect

from data.payment_data import (
    PAYMENT_CARD_VISA_VALIDO,
    PAYMENT_DATA_ENTREGA_REGEX,
)
from utils.payment_steps import (
    click_finalizar_assinatura,
    expect_assinatura_confirmada,
    expect_pagamento_step,
    fill_cartao,
    go_to_payment_step,
)


def test_ct001_assinatura_com_sucesso_fluxo_completo(page: Page):
    go_to_payment_step(page)
    expect_pagamento_step(page)

    fill_cartao(page, numero=PAYMENT_CARD_VISA_VALIDO)
    click_finalizar_assinatura(page)

    confirmada = expect_assinatura_confirmada(page)

    for heading in ("Plano", "Frequência", "Endereço de Entrega", "Próxima Entrega"):
        expect(page.get_by_role("heading", name=heading, level=3)).to_be_visible()

    expect(page.get_by_text(PAYMENT_DATA_ENTREGA_REGEX)).to_be_visible()
    expect(confirmada).to_be_visible()
