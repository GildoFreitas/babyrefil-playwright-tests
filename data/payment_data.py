"""
Constantes para testes do fluxo de pagamento (alinhadas a docs/test-cases.md — seção Pagamento).
"""

import re

# --- Massa: dados do titular do cartão (padrão documentação) ---
PAYMENT_NOME_TITULAR = "João da Silva"
PAYMENT_CPF = "111.111.111-11"
PAYMENT_VALIDADE_FUTURA = "12/30"
PAYMENT_CVV = "182"

# --- CT001: cartão válido (Visa) — pagamento aprovado ---
PAYMENT_CARD_VISA_VALIDO = "4242 4242 4242 4242"

# --- CT002: cartão inválido (Mastercard) — saldo insuficiente ---
PAYMENT_CARD_MASTERCARD_SALDO_INSUFICIENTE = "5555 5555 5555 4444"

# --- CT016: massa inválida (formato malformado dispara as mesmas mensagens do campo vazio) ---
# Valores curtos/fora do formato esperado, garantindo erro determinístico no validador (Zod) sem
# depender de chamada a gateway de pagamento.
PAYMENT_CARD_NUMBER_INVALIDO = "1234"
PAYMENT_VALIDADE_INVALIDA = "13/00"
PAYMENT_CVV_INVALIDO = "12"
PAYMENT_CPF_INVALIDO = "123"

# --- Mensagens de validação exibidas pela UI (Zod / formulário) ---
# Mesma cópia para campo vazio ou valor com formato inválido.
VALIDATION_MSG_CARD_NUMBER_INVALIDO = "Número do cartão inválido."
VALIDATION_MSG_NOME_CARTAO_OBRIGATORIO = "Nome no cartão é obrigatório."
VALIDATION_MSG_VALIDADE_INVALIDA = "Validade inválida (MM/AA)."
VALIDATION_MSG_CVV_INVALIDO = "CVV inválido."
VALIDATION_MSG_CPF_INVALIDO = "CPF inválido."

# --- CT002: toast de pagamento recusado ---
PAYMENT_MSG_TRANSACAO_NAO_AUTORIZADA = (
    "Transação não autorizada. Entre em contato com o emissor do cartão."
)

# --- CT001: confirmação da assinatura ---
# Número do pedido no formato BR + 13 dígitos (ex.: BR1761410590280).
PAYMENT_PEDIDO_NUMERO_REGEX = re.compile(r"^Pedido nº BR\d{13}$")
# Data por extenso em pt-BR (ex.: "sexta-feira, 15 de maio de 2026") — checa o trecho "<dia> de <mês> de <ano>".
PAYMENT_DATA_ENTREGA_REGEX = re.compile(r"\d{1,2} de \w+ de \d{4}")
