"""
Constantes compartilhadas para testes do fluxo de assinatura (alinhadas a docs/test-cases.md).
"""

# --- Massa: dados pessoais / bebê (padrão documentação) ---
SUBSCRIPTION_NOME_COMPLETO = "João da Silva"
SUBSCRIPTION_EMAIL = "joao.silva@email.com"
SUBSCRIPTION_TELEFONE = "11999999999"
SUBSCRIPTION_NOME_BEBE = "Miguel"

# Massa "6 meses" → opção de faixa etária exibida no combobox da UI
SUBSCRIPTION_IDADE_FAIXA_OPTION = "3-6 meses"

# --- Validação (trecho estável) ---
VALIDATION_MSG_NOME_COMPLETO_OBRIGATORIO = "Nome completo é obrigatório."
# Campo vazio dispara validação de e-mail no app (Zod), não o texto "obrigatório".
VALIDATION_MSG_EMAIL_OBRIGATORIO = "E-mail inválido."
# Telefone vazio / curto: mesma lógica (ex.: min(10)); mensagem na UI.
VALIDATION_MSG_TELEFONE_OBRIGATORIO = "Telefone inválido."
# Mensagens exibidas pelo app (copy com "bebê" em minúsculas no texto de erro).
VALIDATION_MSG_NOME_BEBE_OBRIGATORIO = "Nome do bebê é obrigatório."
VALIDATION_MSG_IDADE_BEBE_OBRIGATORIA = "Idade do bebê é obrigatória."

# Placeholder do combobox de idade (CT012 — não selecionado)
SUBSCRIPTION_IDADE_PLACEHOLDER = "Selecione a faixa etária"
