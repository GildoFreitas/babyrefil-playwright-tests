# 📄 Complete Test Case Documentation - BabyRefil

## 🌐 Environment and Test Data

### System URL

- **Test Environment:** `https://babyrefil.vercel.app`

---

# 📦 Available Plans

| Plan | Price (per delivery) | Main Details |
| --- | --- | --- |
| **Essencial** | R$ 119,90 | 2 premium diaper packs, 4 wet wipe packs, 1 diaper rash cream |
| **Conforto** (Popular) | R$ 219,90 | 4 premium diaper packs, 6 hypoallergenic wet wipes, 2 premium creams, bonus items |
| **Completo** | R$ 319,90 | 6 ultra-soft diaper packs, 8 hypoallergenic wet wipes, 3 premium creams, baby care kit, gift, free shipping |

---

# 📍 Test Data: Delivery Address

| Field | Value |
| --- | --- |
| **CEP** | `04534-011` |
| **Rua** | Rua Joaquim Floriano |
| **Número** | 1000 |
| **Complemento** | 17th floor |
| **Bairro** | Itaim Bibi |
| **Cidade** | São Paulo |
| **Estado** | SP |

---

# 👤 Test Data: Personal Information

| Field | Value |
| --- | --- |
| **Nome completo** | João da Silva |
| **Email** | joao.silva@email.com |
| **Telefone** | 11999999999 |
| **Nome do bebê** | Miguel |
| **Idade do bebê** | 6 months |

---

# 💳 Test Data: Credit Cards

| Scenario | Brand | Number | CVV | Expiration Date |
| --- | --- | --- | --- | --- |
| **Valid (Success)** | Visa | `4242424242424242` | `182` | Any future date |
| **Invalid (Insufficient Funds)** | Mastercard | `5555555555554444` | `182` | Any future date |

---

# 🧪 Test Cases - Checkout Flow

---

## CT001: Successful Subscription Checkout (Complete End-to-End Flow)

### Objective

Verify the complete subscription checkout flow using valid data.

### Preconditions

1. The user has valid registration, address, and payment data.
2. The user has a valid credit card.

### Test Data

| Step | Action | Expected Result |
| --- | --- | --- |
| 1 | Click the "Assinar Agora" button (header). | The user should be redirected to the plan selection step. The Essencial, Conforto, and Completo plans should be displayed. |
| 2 | Select an available plan. | The user should proceed to the recurrence selection step. |
| 3 | Select a recurrence option and continue. | The system should correctly update the pricing and proceed with the flow. |
| 4 | Fill in all valid personal information fields. | The system should allow the user to continue the flow. |
| 5 | Fill in a valid delivery address. | The system should allow the user to continue the flow. |
| 6 | Fill in all payment fields using the **Valid (Visa)** card test data. | The system should correctly accept the payment information. |
| 7 | Click "Finalizar Assinatura". | The payment should be successfully approved. |
| 8 | Verify the confirmation screen. | 1. The payment is successfully processed.<br>2. The confirmation appears in the same subscribe flow (URL stays on `/subscribe`); the screen shows the success state (e.g. heading **Assinatura confirmada!**).<br>3. The confirmation area displays the plan summary and estimated delivery date.<br>4. An order reference is shown matching the pattern **Pedido nº BR** + 13 digits (example: **BR1761410590280**). |

---

## CT002: Subscription Checkout Failure Due to Insufficient Funds

### Objective

Verify the system behavior when processing a payment with insufficient funds.

### Preconditions

1. The user has valid registration and address information.
2. The user has a credit card configured for the insufficient funds scenario.

### Test Data

| Field | Value |
| --- | --- |
| Credit Card | 5555555555554444 |
| Scenario | Insufficient funds |

| Step | Action | Expected Result |
| --- | --- | --- |
| 1 | Start the subscription flow. | The plan selection screen should be displayed. The Essencial, Conforto, and Completo plans should be visible. |
| 2 | Select a plan and recurrence option. | The flow should proceed correctly. |
| 3 | Fill in valid personal information. | The system should allow the user to continue. |
| 4 | Fill in a valid address. | The system should allow the user to continue. |
| 5 | Fill in all payment fields using the **Invalid (Insufficient Funds)** card test data. | The payment information should be accepted for processing. |
| 6 | Click "Finalizar Assinatura". | The payment should be declined. |
| 7 | Verify the error message. | The message "**Transação não autorizada. Entre em contato com o emissor do cartão.**" should be displayed informing the payment failure. |
| 8 | Verify that the user remains on the payment screen. | The user should remain on the payment step. |

---

# 🧪 Test Cases - Navigation

---

## CT003: Verify "Como funciona" Button Navigation

### Objective

Verify that the "Como funciona" button correctly redirects the user to the corresponding page section.

### Preconditions

1. The user accesses the system homepage.

| Step | Action | Expected Result |
| --- | --- | --- |
| 1 | Access the BabyRefil homepage. | The homepage should load successfully. |
| 2 | Click the "Como funciona" button in the top navigation menu. | The user should be redirected to the "Como funciona" section. |
| 3 | Verify the displayed section content. | The section information should be displayed correctly. |

---

## CT004: Verify "Planos" Button Navigation

### Objective

Verify that the "Planos" button correctly redirects the user to the plans section.

### Preconditions

1. The user accesses the system homepage.

| Step | Action | Expected Result |
| --- | --- | --- |
| 1 | Access the BabyRefil homepage. | The homepage should load successfully. |
| 2 | Click the "Planos" button. | The user should be redirected to the plans section. |
| 3 | Verify the available plans. | The Essencial, Conforto, and Completo plans should be displayed correctly. |

---

## CT005: Verify "FAQ" Button Navigation

### Objective

Verify that the "FAQ" button correctly redirects the user to the FAQ section.

### Preconditions

1. The user accesses the system homepage.

| Step | Action | Expected Result |
| --- | --- | --- |
| 1 | Access the BabyRefil homepage. | The homepage should load successfully. |
| 2 | Click the "FAQ" button. | The user should be redirected to the FAQ section. |
| 3 | Verify the FAQ section content. | The questions and answers should be displayed correctly. |

---

## CT006: Verify Header "Assinar Agora" Button

### Objective

Verify that the header "Assinar Agora" button correctly starts the subscription flow.

### Preconditions

1. The user accesses the system homepage.

| Step | Action | Expected Result |
| --- | --- | --- |
| 1 | Access the BabyRefil homepage. | The homepage should load successfully. |
| 2 | Click the header "Assinar Agora" button. | The user should be redirected to the subscription flow. |
| 3 | Verify the plan selection screen. | The available plans should be displayed correctly. |

---

## CT007: Verify "Assinar agora" Button in the Plans Section

### Objective

Verify that the "Assinar agora" link in the plans section (sentence case on this CTA) correctly starts the subscription flow.

### Preconditions

1. The user accesses the system homepage.

| Step | Action | Expected Result |
| --- | --- | --- |
| 1 | Access the BabyRefil homepage. | The homepage should load successfully. |
| 2 | Navigate to the plans section. | The section should be displayed correctly. |
| 3 | Click "Assinar agora" for an available plan. | The subscription flow should start successfully. |
| 4 | Verify the recurrence step. | The subscribe wizard should show **Recorrência** in the stepper (together with the plan step), confirming the flow includes recurrence. |

---

# 🧪 Test Cases - Personal Information

---

## CT008: Verify Required "Nome completo" Field

### Objective

Verify that the system does not allow the user to continue without filling in the "Nome completo" field.

### Preconditions

1. The user accessed the homepage.
2. The user clicked "Assinar Agora".
3. The user selected a valid plan.
4. The user selected monthly recurrence.
5. The user proceeded to the "Informações pessoais" step.

### Test Data

| Field | Value |
| --- | --- |
| Nome completo | Em branco |
| Email | joao.silva@email.com |
| Telefone | 11999999999 |
| Nome do bebê | Miguel |
| Idade do bebê | 6 months |

| Step | Action | Expected Result |
| --- | --- | --- |
| 1 | Fill in all required fields except "Nome completo". | The form should remain incomplete. |
| 2 | Click "Continuar". | The system should prevent the user from proceeding. |
| 3 | Verify the error message. | A required field validation message should be displayed. |

---

## CT009: Verify Required "Email" Field

### Objective

Verify that the system does not allow the user to continue without filling in the "Email" field.

### Preconditions

1. The user accessed the homepage.
2. The user clicked "Assinar Agora".
3. The user selected a valid plan.
4. The user selected monthly recurrence.
5. The user proceeded to the "Informações pessoais" step.

### Test Data

| Field | Value |
| --- | --- |
| Nome completo | João da Silva |
| Email | Em branco |
| Telefone | 11999999999 |
| Nome do bebê | Miguel |
| Idade do bebê | 6 months |

| Step | Action | Expected Result |
| --- | --- | --- |
| 1 | Fill in all required fields except "Email". | The form should remain incomplete. |
| 2 | Click "Continuar". | The system should prevent the user from proceeding. |
| 3 | Verify the error message. | A required field validation message should be displayed. |

---

## CT010: Verify Required "Telefone" Field

### Objective

Verify that the system does not allow the user to continue without filling in the "Telefone" field.

### Preconditions

1. The user accessed the homepage.
2. The user clicked "Assinar Agora".
3. The user selected a valid plan.
4. The user selected monthly recurrence.
5. The user proceeded to the "Informações pessoais" step.

### Test Data

| Field | Value |
| --- | --- |
| Nome completo | João da Silva |
| Email | joao.silva@email.com |
| Telefone | Em branco |
| Nome do bebê | Miguel |
| Idade do bebê | 6 months |

| Step | Action | Expected Result |
| --- | --- | --- |
| 1 | Fill in all required fields except "Telefone". | The form should remain incomplete. |
| 2 | Click "Continuar". | The system should prevent the user from proceeding. |
| 3 | Verify the error message. | A required field validation message should be displayed. |

---

## CT011: Verify Required "Nome do bebê" Field

### Objective

Verify that the system does not allow the user to continue without filling in the "Nome do bebê" field.

### Preconditions

1. The user accessed the homepage.
2. The user clicked "Assinar Agora".
3. The user selected a valid plan.
4. The user selected monthly recurrence.
5. The user proceeded to the "Informações pessoais" step.

### Test Data

| Field | Value |
| --- | --- |
| Nome completo | João da Silva |
| Email | joao.silva@email.com |
| Telefone | 11999999999 |
| Nome do bebê | Em branco |
| Idade do bebê | 6 months |

| Step | Action | Expected Result |
| --- | --- | --- |
| 1 | Fill in all required fields except "Nome do bebê". | The form should remain incomplete. |
| 2 | Click "Continuar". | The system should prevent the user from proceeding. |
| 3 | Verify the error message. | A required field validation message should be displayed. |

---

## CT012: Verify Required "Idade do bebê" Field

### Objective

Verify that the system does not allow the user to continue without selecting the baby's age.

### Preconditions

1. The user accessed the homepage.
2. The user clicked "Assinar Agora".
3. The user selected a valid plan.
4. The user selected monthly recurrence.
5. The user proceeded to the "Informações pessoais" step.

### Test Data

| Field | Value |
| --- | --- |
| Nome completo | João da Silva |
| Email | joao.silva@email.com |
| Telefone | 11999999999 |
| Nome do bebê | Miguel |
| Idade do bebê | Não selecionado |

| Step | Action | Expected Result |
| --- | --- | --- |
| 1 | Fill in all required fields except "Idade do bebê". | The form should remain incomplete. |
| 2 | Click "Continuar". | The system should prevent the user from proceeding. |
| 3 | Verify the error message. | A required field validation message should be displayed. |

---

# 🧪 Test Cases - Address

---

## CT013: Verify Required or Invalid CEP

### Objective

Verify that the system does not allow the user to continue with a blank or invalid CEP.

### Preconditions

1. The user accessed the homepage.
2. The user clicked "Assinar Agora".
3. The user selected a valid plan.
4. The user selected monthly recurrence.
5. The user proceeded to the "Endereço" step.

### Test Data

| Field | Value |
| --- | --- |
| CEP | Em branco ou inválido |

| Step | Action | Expected Result |
| --- | --- | --- |
| 1 | Leave the CEP field blank or enter an invalid CEP. | The form should remain invalid. |
| 2 | Click "Continuar". | The system should prevent the user from proceeding. |
| 3 | Verify the error message. | A validation message indicating invalid or required CEP should be displayed. |

---

## CT014: Verify Automatic Address Autofill by CEP

### Objective

Verify that the system automatically fills in the address information after entering a valid CEP.

### Preconditions

1. The user accessed the homepage.
2. The user clicked "Assinar Agora".
3. The user selected a valid plan.
4. The user selected monthly recurrence.
5. The user proceeded to the "Endereço" step.

### Test Data

| Field | Value |
| --- | --- |
| CEP | 04534-011 |
| Rua | Rua Joaquim Floriano |
| Bairro | Itaim Bibi |
| Cidade | São Paulo |
| Estado | SP |

| Step | Action | Expected Result |
| --- | --- | --- |
| 1 | Enter a valid CEP. | No automatic action should occur before clicking the search button. |
| 2 | Click the "Buscar CEP" button. | The address fields should be automatically populated. |
| 3 | Wait for the autofill process to complete. | The address fields should be automatically populated. |
| 4 | Verify the populated data. | Rua, bairro, cidade, and estado fields should contain the correct values. |

---

## CT015: Verify Required Address Fields

### Objective

Verify that the system does not allow the user to continue without filling in the required address fields.

### Preconditions

1. The user accessed the homepage.
2. The user clicked "Assinar Agora".
3. The user selected a valid plan.
4. The user selected monthly recurrence.
5. The user proceeded to the "Endereço" step.

### Test Data

| Field | Value |
| --- | --- |
| CEP | 04534-011 |
| Rua | Em branco |
| Número | Em branco |
| Bairro | Em branco |
| Cidade | Em branco |
| Estado | Em branco |

| Step | Action | Expected Result |
| --- | --- | --- |
| 1 | Enter a valid CEP. | No automatic action should occur before clicking the search button. |
| 2 | Leave required address fields blank. | The form should remain incomplete. |
| 3 | Click "Continuar". | The system should prevent the user from proceeding. |
| 4 | Verify the error messages. | Validation messages indicating required fields should be displayed. |

---

# 🧪 Test Cases - Payment

---

## CT016: Verify Required Credit Card Fields

### Objective

Verify that the system does not allow the user to complete the subscription without correctly filling in the credit card information.

### Preconditions

1. The user accessed the homepage.
2. The user clicked "Assinar Agora".
3. The user selected a valid plan.
4. The user selected monthly recurrence.
5. The user proceeded to the "Pagamento" step.
6. The user filled in all previous fields with valid information.
7. The user proceeded to the payment step.

### Test Data

| Field | Value |
| --- | --- |
| Número do cartão | Em branco ou inválido |
| Nome impresso no cartão | Em branco |
| Validade | Inválida |
| CVV | Invalid |
| CPF | Invalid |

| Step | Action | Expected Result |
| --- | --- | --- |
| 1 | Leave credit card fields blank or invalid. | The form should remain invalid. |
| 2 | Click "Finalizar Assinatura". | The system should prevent the subscription from being completed. |
| 3 | Verify the error messages. | Validation messages indicating required or invalid fields should be displayed. |