"""
Address flow constants (aligned with docs/test-cases.md — Address section).

UI-facing string values below are Portuguese literals as shown in the app.
"""

# Too-short / invalid mask — triggers the same validation as an empty CEP in the UI.
ADDRESS_CEP_MALFORMED = "123"

# App copy (Zod / form) for missing or invalid CEP format.
VALIDATION_MSG_CEP_INVALIDO = "CEP inválido."

# CT014: valid CEP + autofill (ViaCEP / Buscar button).
ADDRESS_CEP_VALIDO_AUTOCOMPLETE = "04534-011"
ADDRESS_RUA_ESPERADA = "Rua Joaquim Floriano"
ADDRESS_BAIRRO_ESPERADO = "Itaim Bibi"
ADDRESS_CIDADE_ESPERADA = "São Paulo"
ADDRESS_ESTADO_ESPERADO = "SP"

# Editable fields (number / complement — documentation sample).
ADDRESS_NUMERO = "1000"
ADDRESS_COMPLEMENTO = "17o andar"

# CT015: incomplete address (CEP filled, Search not used, other required lines empty).
VALIDATION_MSG_ENDERECO_OBRIGATORIO = "Endereço é obrigatório."
VALIDATION_MSG_NUMERO_OBRIGATORIO = "Número é obrigatório."
VALIDATION_MSG_BAIRRO_OBRIGATORIO = "Bairro é obrigatório."
VALIDATION_MSG_CIDADE_OBRIGATORIA = "Cidade é obrigatória."
VALIDATION_MSG_ESTADO_OBRIGATORIO = "Estado é obrigatório."
