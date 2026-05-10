"""
CT002 — Adesão com Falha de Pagamento (Saldo Insuficiente) (test-cases.md, Fluxo de Assinatura).

Pré-condições: etapa "Pagamento" via `go_to_payment_step` em utils/payment_steps.py
(percorre Plano → Recorrência → Dados Pessoais → Endereço com a massa padrão).

Cenário: cartão Mastercard de saldo insuficiente (`PAYMENT_CARD_MASTERCARD_SALDO_INSUFICIENTE`)
→ pagamento recusado, exibindo o toast "Transação não autorizada. Entre em contato com o emissor
do cartão." e mantendo o usuário na etapa de pagamento.

Nota de alinhamento com a UI: o caso fala em "Confirmar Pagamento"; o CTA real é "Finalizar Assinatura".
A mensagem de erro aparece via toast (sonner) na região "Notifications" — pode auto-dismiss.

Riscos de flake:
- Toast aparece após resposta do gateway simulado; default timeout do `expect` (5s) é suficiente.
- Toast pode somar-se a outros pop-ups; usamos texto exato da descrição para isolar.
"""

from __future__ import annotations

from playwright.sync_api import Page, expect

from data.payment_data import (
    PAYMENT_CARD_MASTERCARD_SALDO_INSUFICIENTE,
    PAYMENT_MSG_TRANSACAO_NAO_AUTORIZADA,
)
from utils.navigation import expect_subscribe_url
from utils.payment_steps import (
    click_finalizar_assinatura,
    expect_pagamento_step,
    fill_cartao,
    go_to_payment_step,
)


def test_ct002_pagamento_recusado_saldo_insuficiente(page: Page):
    go_to_payment_step(page)
    finalizar = expect_pagamento_step(page)

    fill_cartao(page, numero=PAYMENT_CARD_MASTERCARD_SALDO_INSUFICIENTE)
    click_finalizar_assinatura(page)

    expect(page.get_by_text(PAYMENT_MSG_TRANSACAO_NAO_AUTORIZADA, exact=True)).to_be_visible()

    expect(finalizar).to_be_visible()
    expect_subscribe_url(page)
