# 📄 Documentação Completa de Casos de Teste - BabyRefil

## 🌐 Ambiente e Dados de Teste

### URL do Sistema

- **Ambiente de Testes:** `https://babyrefil.vercel.app`

---

# 📦 Planos Disponíveis

| Plano | Valor (por entrega) | Detalhes Principais |
| --- | --- | --- |
| **Essencial** | R$ 119,90 | 2 pacotes de fralda premium, 4 pacotes de lenço umedecido, 1 pomada |
| **Conforto** (Popular) | R$ 219,90 | 4 pacotes de fralda premium, 6 lenços hipoalergênico, 2 pomadas premium, mimos |
| **Completo** | R$ 319,90 | 6 pacotes de fralda ultra macia, 8 lenços hipoalergênico, 3 pomadas premium, kit cuidados, brinde, frete grátis |

---

# 📍 Massa de Dados: Endereço de Entrega

| Campo | Valor |
| --- | --- |
| **CEP** | `04534-011` |
| **Logradouro** | Rua Joaquim Floriano |
| **Número** | 1000 |
| **Complemento** | 17o andar |
| **Bairro** | Itaim Bibi |
| **Cidade** | São Paulo |
| **Estado** | SP |

---

# 👤 Massa de Dados: Dados Pessoais

| Campo | Valor |
| --- | --- |
| **Nome Completo** | João da Silva |
| **Email** | joao.silva@email.com |
| **Telefone** | 11999999999 |
| **Nome do Bebê** | Miguel |
| **Idade do Bebê** | 6 meses |

---

# 💳 Massa de Dados: Cartões de Crédito

| Cenário | Bandeira | Número | CVV | Validade |
| --- | --- | --- | --- | --- |
| **Válido (Sucesso)** | Visa | `4242424242424242` | `182` | Qualquer data futura |
| **Inválido (Saldo Insuf.)** | Mastercard | `5555555555554444` | `182` | Qualquer data futura |

---

# 🧪 Casos de Teste - Fluxo de Assinatura

---

## CT001: Adesão de Assinatura com Sucesso (Fluxo Completo)

### Objetivo

Validar o fluxo completo de assinatura com sucesso utilizando dados válidos.

### Pré-condições

1. Usuário possui dados válidos de cadastro, endereço e pagamento.
2. Usuário possui cartão válido.

### Massa de Dados

| Passo | Ação | Resultado Esperado |
| --- | --- | --- |
| 1 | Clicar no botão "Assinar Agora". | O usuário deve ser direcionado para a etapa de seleção de plano. Deve exibir os planos **Essencial, Conforto e Completo.** |
| 2 | Selecionar um plano disponível. | O usuário deve avançar para seleção de recorrência. |
| 3 | Selecionar uma recorrência e avançar. | O sistema deve atualizar os valores corretamente e avançar o fluxo. |
| 4 | Preencher todos os dados pessoais válidos. | O sistema deve permitir continuar o fluxo. |
| 5 | Preencher endereço válido. | O sistema deve permitir continuar o fluxo. |
| 6 | Preencher todos os campos de pagamento com os dados do cartão **Válido (Visa)** da massa de dados.| O sistema deve aceitar os dados corretamente. |
| 7 | Clicar em "Confirmar Pagamento". | O pagamento deve ser aprovado com sucesso. |
| 8 | Validar tela de confirmação. | 1. O pagamento é processado com sucesso.
2. O usuário é redirecionado para a página de confirmação de assinatura.
3. A página de confirmação exibe o resumo do plano e a data estimada de entrega.
4. Deve ser exibido o numero do pedido no formato **BR1761410590280**.|

---

## CT002: Adesão com Falha de Pagamento (Saldo Insuficiente)

### Objetivo

Validar o comportamento do sistema ao processar pagamento com saldo insuficiente.

### Pré-condições

1. Usuário possui dados válidos de cadastro e endereço.
2. Usuário possui cartão inválido para saldo insuficiente.

### Massa de Dados

| Campo | Valor |
| --- | --- |
| Cartão | 5555555555554444 |
| Cenário | Saldo insuficiente |

| Passo | Ação | Resultado Esperado |
| --- | --- | --- |
| 1 | Iniciar fluxo de assinatura. | A tela de seleção de plano deve ser exibida. Deve exibir os planos **Essencial, Conforto e Completo.**|
| 2 | Selecionar plano e recorrência. | O fluxo deve avançar corretamente. |
| 3 | Preencher dados pessoais válidos. | O sistema deve permitir continuar. |
| 4 | Preencher endereço válido. | O sistema deve permitir continuar. |
| 5 | Preencher todos os campos de pagamento com os dados do cartão **Inválido (Saldo Insuf.)** da massa de dados.| Os dados devem ser aceitos para processamento. |
| 6 | Clicar em "Confirmar Pagamento". | O pagamento deve ser recusado. |
| 7 | Validar mensagem de erro. | Deve ser exibida a mensagem "**Transação não autorizada. Entre em contato com o emissor do cartão.**" informando falha de pagamento |
| 8 | Validar permanência na tela de pagamento. | O usuário deve permanecer na etapa de pagamento. |

---

# 🧪 Casos de Teste - Navegação

---

## CT003: Validar Navegação do Botão "Como Funciona"

### Objetivo

Validar que o botão "Como Funciona" redireciona corretamente o usuário para a seção correspondente da página.

### Pré-condições

1. Usuário deve acessar a homepage do sistema.

| Passo | Ação | Resultado Esperado |
| --- | --- | --- |
| 1 | Acessar a homepage do BabyRefil. | A homepage deve ser carregada corretamente. |
| 2 | Clicar no botão "Como Funciona" no menu superior. | O usuário deve ser direcionado para a seção "Como Funciona". |
| 3 | Validar conteúdo da seção exibida. | As informações da seção devem ser exibidas corretamente. |

---

## CT004: Validar Navegação do Botão "Planos"

### Objetivo

Validar que o botão "Planos" redireciona corretamente o usuário para a seção de planos.

### Pré-condições

1. Usuário deve acessar a homepage do sistema.

| Passo | Ação | Resultado Esperado |
| --- | --- | --- |
| 1 | Acessar a homepage do BabyRefil. | A homepage deve ser carregada corretamente. |
| 2 | Clicar no botão "Planos". | O usuário deve ser direcionado para a seção de planos. |
| 3 | Validar planos disponíveis. | Os planos Essencial, Conforto e Completo devem ser exibidos corretamente. |

---

## CT005: Validar Navegação do Botão "FAQ"

### Objetivo

Validar que o botão "FAQ" redireciona corretamente o usuário para a seção FAQ.

### Pré-condições

1. Usuário deve acessar a homepage do sistema.

| Passo | Ação | Resultado Esperado |
| --- | --- | --- |
| 1 | Acessar a homepage do BabyRefil. | A homepage deve ser carregada corretamente. |
| 2 | Clicar no botão "FAQ". | O usuário deve ser direcionado para a seção FAQ. |
| 3 | Validar conteúdo FAQ. | As perguntas e respostas devem ser exibidas corretamente. |

---

## CT006: Validar Botão "Assine Agora" do Header

### Objetivo

Validar que o botão "Assine Agora" do topo da página inicia corretamente o fluxo de assinatura.

### Pré-condições

1. Usuário deve acessar a homepage do sistema.

| Passo | Ação | Resultado Esperado |
| --- | --- | --- |
| 1 | Acessar a homepage do BabyRefil. | A homepage deve ser carregada corretamente. |
| 2 | Clicar no botão "Assine Agora" do header. | O usuário deve ser direcionado para o fluxo de assinatura. |
| 3 | Validar tela de seleção de planos. | Os planos devem ser exibidos corretamente. |

---

## CT007: Validar Botão "Assine Agora" da Seção de Planos

### Objetivo

Validar que o botão "Assine Agora" da seção de planos inicia corretamente o fluxo de assinatura.

### Pré-condições

1. Usuário deve acessar a homepage do sistema.

| Passo | Ação | Resultado Esperado |
| --- | --- | --- |
| 1 | Acessar a homepage do BabyRefil. | A homepage deve ser carregada corretamente. |
| 2 | Navegar até a seção de planos. | A seção deve ser exibida corretamente. |
| 3 | Clicar em "Assine Agora" de um plano disponível. | O fluxo de assinatura deve iniciar corretamente. |
| 4 | Validar etapa de recorrência. | A tela de recorrência deve ser exibida corretamente. |

---

# 🧪 Casos de Teste - Dados Pessoais

---

## CT008: Validar Campo "Nome Completo" Obrigatório

### Objetivo

Validar que o sistema não permite continuar sem preencher o campo "Nome Completo".

### Massa de Dados

| Campo | Valor |
| --- | --- |
| Nome Completo | Em branco |
| Email | joao.silva@email.com |
| Telefone | 11999999999 |
| Nome do Bebê | Miguel |
| Idade do Bebê | 6 meses |

| Passo | Ação | Resultado Esperado |
| --- | --- | --- |
| 1 | Preencher todos os campos obrigatórios exceto "Nome Completo". | O formulário deve permanecer incompleto. |
| 2 | Clicar em avançar. | O sistema deve impedir o avanço do fluxo. |
| 3 | Validar mensagem de erro. | Deve ser exibida mensagem indicando campo obrigatório. |

---

## CT009: Validar Campo "Email" Obrigatório

### Objetivo

Validar que o sistema não permite continuar sem preencher o campo "Email".

### Massa de Dados

| Campo | Valor |
| --- | --- |
| Nome Completo | João da Silva |
| Email | Em branco |
| Telefone | 11999999999 |
| Nome do Bebê | Miguel |
| Idade do Bebê | 6 meses |

| Passo | Ação | Resultado Esperado |
| --- | --- | --- |
| 1 | Preencher todos os campos obrigatórios exceto "Email". | O formulário deve permanecer incompleto. |
| 2 | Clicar em avançar. | O sistema deve impedir o avanço do fluxo. |
| 3 | Validar mensagem de erro. | Deve ser exibida mensagem indicando campo obrigatório. |

---

## CT010: Validar Campo "Telefone" Obrigatório

### Objetivo

Validar que o sistema não permite continuar sem preencher o campo "Telefone".

### Massa de Dados

| Campo | Valor |
| --- | --- |
| Nome Completo | João da Silva |
| Email | joao.silva@email.com |
| Telefone | Em branco |
| Nome do Bebê | Miguel |
| Idade do Bebê | 6 meses |

| Passo | Ação | Resultado Esperado |
| --- | --- | --- |
| 1 | Preencher todos os campos obrigatórios exceto "Telefone". | O formulário deve permanecer incompleto. |
| 2 | Clicar em avançar. | O sistema deve impedir o avanço do fluxo. |
| 3 | Validar mensagem de erro. | Deve ser exibida mensagem indicando campo obrigatório. |

---

## CT011: Validar Campo "Nome do Bebê" Obrigatório

### Objetivo

Validar que o sistema não permite continuar sem preencher o campo "Nome do Bebê".

### Massa de Dados

| Campo | Valor |
| --- | --- |
| Nome Completo | João da Silva |
| Email | joao.silva@email.com |
| Telefone | 11999999999 |
| Nome do Bebê | Em branco |
| Idade do Bebê | 6 meses |

| Passo | Ação | Resultado Esperado |
| --- | --- | --- |
| 1 | Preencher todos os campos obrigatórios exceto "Nome do Bebê". | O formulário deve permanecer incompleto. |
| 2 | Clicar em avançar. | O sistema deve impedir o avanço do fluxo. |
| 3 | Validar mensagem de erro. | Deve ser exibida mensagem indicando campo obrigatório. |

---

## CT012: Validar Campo "Idade do Bebê" Obrigatório

### Objetivo

Validar que o sistema não permite continuar sem selecionar a idade do bebê.

### Massa de Dados

| Campo | Valor |
| --- | --- |
| Nome Completo | João da Silva |
| Email | joao.silva@email.com |
| Telefone | 11999999999 |
| Nome do Bebê | Miguel |
| Idade do Bebê | Não selecionado |

| Passo | Ação | Resultado Esperado |
| --- | --- | --- |
| 1 | Preencher todos os campos obrigatórios exceto "Idade do Bebê". | O formulário deve permanecer incompleto. |
| 2 | Clicar em avançar. | O sistema deve impedir o avanço do fluxo. |
| 3 | Validar mensagem de erro. | Deve ser exibida mensagem indicando campo obrigatório. |

---

# 🧪 Casos de Teste - Endereço

---

## CT013: Validar CEP Obrigatório ou Inválido

### Objetivo

Validar que o sistema não permite continuar com CEP vazio ou inválido.

### Massa de Dados

| Campo | Valor |
| --- | --- |
| CEP | Em branco ou inválido |

| Passo | Ação | Resultado Esperado |
| --- | --- | --- |
| 1 | Deixar o campo CEP vazio ou preencher com CEP inválido. | O formulário deve permanecer inválido. |
| 2 | Clicar em avançar. | O sistema deve impedir o avanço do fluxo. |
| 3 | Validar mensagem de erro. | Deve ser exibida mensagem indicando CEP inválido ou obrigatório. |

---

## CT014: Validar Preenchimento Automático de Endereço pelo CEP

### Objetivo

Validar que o sistema preenche automaticamente os dados do endereço após informar um CEP válido.

### Massa de Dados

| Campo | Valor |
| --- | --- |
| CEP | 04534-011 |
| Rua | Rua Joaquim Floriano |
| Bairro | Itaim Bibi |
| Cidade | São Paulo |
| Estado | SP |

| Passo | Ação | Resultado Esperado |
| --- | --- | --- |
| 1 | Informar CEP válido. | O sistema não deve fazer nada |
| 2 | Clicar no botão "Buscar" | Os campos devem ser preenchidos automaticamente. |
| 3 | Aguardar preenchimento automático. | Os campos devem ser preenchidos automaticamente. |
| 4 | Validar dados preenchidos. | Rua, bairro, cidade e estado devem conter os valores corretos. |

---

## CT015: Validar Campos Obrigatórios do Endereço

### Objetivo

Validar que o sistema não permite continuar sem preencher os campos obrigatórios do endereço.

### Massa de Dados

| Campo | Valor |
| --- | --- |
| CEP | 04534-011 |
| Rua | Em branco |
| Número | Em branco |
| Bairro | Em branco |
| Cidade | Em branco |
| Estado | Em branco |

| Passo | Ação | Resultado Esperado |
| --- | --- | --- |
| 1 | Preencher CEP válido. | O sistema não deve fazer nada |
| 2 | Deixar campos obrigatórios em branco. | O formulário deve permanecer incompleto. |
| 3 | Clicar em avançar. | O sistema deve impedir o avanço do fluxo. |
| 4 | Validar mensagens de erro. | Deve ser exibida mensagem indicando campos obrigatórios. |

---

# 🧪 Casos de Teste - Pagamento

---

## CT016: Validar Campos Obrigatórios do Cartão

### Objetivo

Validar que o sistema não permite finalizar assinatura sem preencher corretamente os dados do cartão.

### Massa de Dados

| Campo | Valor |
| --- | --- |
| Número do Cartão | Em branco ou inválido |
| Nome do Titular | Em branco |
| Validade | Inválida |
| CVV | Inválido |
| CPF | Inválido |

| Passo | Ação | Resultado Esperado |
| --- | --- | --- |
| 1 | Deixar campos do cartão vazios ou inválidos. | O formulário deve permanecer inválido. |
| 2 | Clicar em "Confirmar Pagamento". | O sistema deve impedir a finalização da assinatura. |
| 3 | Validar mensagens de erro. | Deve ser exibida mensagem indicando campos obrigatórios ou inválidos. |