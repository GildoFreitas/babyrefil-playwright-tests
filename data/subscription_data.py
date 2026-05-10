"""
Personal / baby data for subscription tests (aligned with docs/test-cases.md).

UI-facing validation strings are Portuguese literals from the app.
"""

# Default personal + baby data (documentation sample).
SUBSCRIPTION_NOME_COMPLETO = "João da Silva"
SUBSCRIPTION_EMAIL = "joao.silva@email.com"
SUBSCRIPTION_TELEFONE = "11999999999"
SUBSCRIPTION_NOME_BEBE = "Miguel"

# "6 months" → age band label shown in the UI combobox.
SUBSCRIPTION_IDADE_FAIXA_OPTION = "3-6 meses"

# Stable validation excerpts (exact UI copy).
VALIDATION_MSG_NOME_COMPLETO_OBRIGATORIO = "Nome completo é obrigatório."
# Empty email: Zod shows invalid email, not the word "obrigatório".
VALIDATION_MSG_EMAIL_OBRIGATORIO = "E-mail inválido."
# Empty / too-short phone: min-length style message in the UI.
VALIDATION_MSG_TELEFONE_OBRIGATORIO = "Telefone inválido."
VALIDATION_MSG_NOME_BEBE_OBRIGATORIO = "Nome do bebê é obrigatório."
VALIDATION_MSG_IDADE_BEBE_OBRIGATORIA = "Idade do bebê é obrigatória."

# CT012 — age not selected: combobox placeholder.
SUBSCRIPTION_IDADE_PLACEHOLDER = "Selecione a faixa etária"
