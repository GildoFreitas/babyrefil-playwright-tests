"""
Payment flow constants (aligned with docs/test-cases.md — Payment section).

Portuguese strings are exact UI copy for assertions. Card numbers use spaced groups as entered in tests.
"""

import re

# Default cardholder data (documentation sample).
PAYMENT_NOME_TITULAR = "João da Silva"
PAYMENT_CPF = "111.111.111-11"
PAYMENT_VALIDADE_FUTURA = "12/30"
PAYMENT_CVV = "182"

# CT001 — approved payment (Visa test card).
PAYMENT_CARD_VISA_VALIDO = "4242 4242 4242 4242"

# CT002 — declined payment (insufficient funds test card).
PAYMENT_CARD_MASTERCARD_SALDO_INSUFICIENTE = "5555 5555 5555 4444"

# CT016 — invalid shapes: short values trigger the same messages as empty fields (Zod), no gateway call.
PAYMENT_CARD_NUMBER_INVALIDO = "1234"
PAYMENT_VALIDADE_INVALIDA = "13/00"
PAYMENT_CVV_INVALIDO = "12"
PAYMENT_CPF_INVALIDO = "123"

# Validation messages (Zod / form); same copy for empty or malformed values where applicable.
VALIDATION_MSG_CARD_NUMBER_INVALIDO = "Número do cartão inválido."
VALIDATION_MSG_NOME_CARTAO_OBRIGATORIO = "Nome no cartão é obrigatório."
VALIDATION_MSG_VALIDADE_INVALIDA = "Validade inválida (MM/AA)."
VALIDATION_MSG_CVV_INVALIDO = "CVV inválido."
VALIDATION_MSG_CPF_INVALIDO = "CPF inválido."

# CT002 — declined payment toast (exact UI string).
PAYMENT_MSG_TRANSACAO_NAO_AUTORIZADA = (
    "Transação não autorizada. Entre em contato com o emissor do cartão."
)

# CT001 — confirmation: order line "Pedido nº BR" + 13 digits.
PAYMENT_PEDIDO_NUMERO_REGEX = re.compile(r"^Pedido nº BR\d{13}$")
# Long date in pt-BR (e.g. "sexta-feira, 15 de maio de 2026"); pattern matches "<day> de <month> de <year>".
PAYMENT_DATA_ENTREGA_REGEX = re.compile(r"\d{1,2} de \w+ de \d{4}")
