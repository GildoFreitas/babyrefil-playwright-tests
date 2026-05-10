"""
CT016 — Validar campos obrigatórios do cartão (test-cases.md).

Pré-condições: etapa "Pagamento" via `go_to_payment_step` em utils/payment_steps.py
(percorre Plano → Recorrência → Dados Pessoais → Endereço com a massa padrão).

Cenários (alinhados à massa do caso):
- Todos os campos do cartão vazios: o app exibe as 5 mensagens de erro do formulário.
- Todos os campos com formato inválido (não-vazio): o app reusa as mesmas mensagens
  (validação Zod por campo, sem chamada a gateway).

Riscos de flake:
- O texto "Pagamento" aparece no indicador de etapa e no título da seção; o checkpoint
  da etapa usa "Resumo do Pedido" + botão "Finalizar Assinatura" (`expect_pagamento_step`).
- Mensagens são parágrafos próximos a cada campo; validamos por texto exato para evitar
  acoplamento a estrutura DOM/aria.
"""

from __future__ import annotations

from playwright.sync_api import Page, expect

from data.payment_data import (
    PAYMENT_CARD_NUMBER_INVALIDO,
    PAYMENT_CPF_INVALIDO,
    PAYMENT_CVV_INVALIDO,
    PAYMENT_VALIDADE_INVALIDA,
    VALIDATION_MSG_CARD_NUMBER_INVALIDO,
    VALIDATION_MSG_CPF_INVALIDO,
    VALIDATION_MSG_CVV_INVALIDO,
    VALIDATION_MSG_NOME_CARTAO_OBRIGATORIO,
    VALIDATION_MSG_VALIDADE_INVALIDA,
)
from utils.navigation import expect_subscribe_url
from utils.payment_steps import (
    click_finalizar_assinatura,
    expect_pagamento_step,
    go_to_payment_step,
)

_VALIDATION_MESSAGES = (
    VALIDATION_MSG_CARD_NUMBER_INVALIDO,
    VALIDATION_MSG_NOME_CARTAO_OBRIGATORIO,
    VALIDATION_MSG_VALIDADE_INVALIDA,
    VALIDATION_MSG_CVV_INVALIDO,
    VALIDATION_MSG_CPF_INVALIDO,
)


def test_ct016_campos_em_branco_pagamento(page: Page):
    go_to_payment_step(page)
    finalizar = expect_pagamento_step(page)

    numero_cartao = page.get_by_label("Número do Cartão")
    nome_cartao = page.get_by_label("Nome no Cartão")
    validade = page.get_by_label("Validade")
    cvv = page.get_by_label("CVV")
    cpf = page.get_by_label("CPF do Titular")

    for campo in (numero_cartao, nome_cartao, validade, cvv, cpf):
        expect(campo).to_be_visible()
        expect(campo).to_have_value("")

    click_finalizar_assinatura(page)

    for msg in _VALIDATION_MESSAGES:
        expect(page.get_by_text(msg, exact=True)).to_be_visible()

    expect(finalizar).to_be_visible()
    expect_subscribe_url(page)


def test_ct016_campos_invalidos_pagamento(page: Page):
    go_to_payment_step(page)
    finalizar = expect_pagamento_step(page)

    page.get_by_label("Número do Cartão").fill(PAYMENT_CARD_NUMBER_INVALIDO)
    page.get_by_label("Validade").fill(PAYMENT_VALIDADE_INVALIDA)
    page.get_by_label("CVV").fill(PAYMENT_CVV_INVALIDO)
    page.get_by_label("CPF do Titular").fill(PAYMENT_CPF_INVALIDO)
    expect(page.get_by_label("Nome no Cartão")).to_have_value("")

    click_finalizar_assinatura(page)

    for msg in _VALIDATION_MESSAGES:
        expect(page.get_by_text(msg, exact=True)).to_be_visible()

    expect(finalizar).to_be_visible()
    expect_subscribe_url(page)
