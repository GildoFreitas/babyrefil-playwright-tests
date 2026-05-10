"""
Constantes para testes do fluxo de endereço (alinhadas a docs/test-cases.md — seção Endereço).
"""

# CEP com formato insuficiente / inválido na máscara — dispara a mesma validação de CEP vazio na UI.
ADDRESS_CEP_MALFORMED = "123"

# Copy exibida pelo app (Zod / formulário) para CEP ausente ou formato inválido.
VALIDATION_MSG_CEP_INVALIDO = "CEP inválido."

# --- CT014: CEP válido + preenchimento automático (ViaCEP / botão Buscar) ---
ADDRESS_CEP_VALIDO_AUTOCOMPLETE = "04534-011"
ADDRESS_RUA_ESPERADA = "Rua Joaquim Floriano"
ADDRESS_BAIRRO_ESPERADO = "Itaim Bibi"
ADDRESS_CIDADE_ESPERADA = "São Paulo"
ADDRESS_ESTADO_ESPERADO = "SP"

# Campos editáveis do endereço (Número/Complemento — massa documentada).
ADDRESS_NUMERO = "1000"
ADDRESS_COMPLEMENTO = "17o andar"

# --- CT015: endereço incompleto (CEP válido informado, sem Buscar — demais obrigatórios vazios) ---
VALIDATION_MSG_ENDERECO_OBRIGATORIO = "Endereço é obrigatório."
VALIDATION_MSG_NUMERO_OBRIGATORIO = "Número é obrigatório."
VALIDATION_MSG_BAIRRO_OBRIGATORIO = "Bairro é obrigatório."
VALIDATION_MSG_CIDADE_OBRIGATORIA = "Cidade é obrigatória."
VALIDATION_MSG_ESTADO_OBRIGATORIO = "Estado é obrigatório."
