"""
Constantes para testes do fluxo de pagamento (alinhadas a docs/test-cases.md — seção Pagamento).
"""

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
