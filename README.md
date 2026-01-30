# Teste PowerOfData

Este projeto é um **proxy de API** simples, construído em **Python**, pensado para ser usado junto ao **Google Cloud Platform (GCP)** e **Apigee**.

Ele expõe uma API intermediária que consome a **SWAPI (Star Wars API)** e serve como base para estudos de:

* API Management (Apigee)
* Proxy / Gateway
* Deploy no GCP
* Boas práticas de estrutura de projeto

---

## 📌 Visão Geral

Arquitetura simplificada:

```
Cliente → Apigee → API Pod (Python) → SWAPI
```

O **Apigee** atua como *API Gateway* (segurança, rate limit, analytics), enquanto o **API Pod** é o backend responsável por fazer a chamada real para a SWAPI.

---

## 🗂 Estrutura do Projeto

```
.
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

### `main.py`

Arquivo principal da aplicação.

* Contém a função `api_pod`
* Define os endpoints
* Faz proxy das requisições para a SWAPI

---

## 🧠 Decisão de Nome: `api_pod` vs `swapi_proxy`

Optei por **`api_pod`** porque:

* Representa melhor o papel do serviço (backend genérico)
* Não acopla o nome apenas à SWAPI
* Facilita reutilização futura com outras APIs

O Apigee pode continuar expondo um nome mais semântico, como:

```
/swapi/people
```

Mesmo que internamente o backend seja o `api_pod`.

---

## ⚙️ Requisitos

* Python **3.10+**
* Conta no **Google Cloud Platform**
* Projeto GCP ativo
* Apigee (Evaluation ou X)

---

## 📦 Instalação Local

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/api-pod.git
cd api-pod
```

### 2️⃣ Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Executar a aplicação

```bash
python main.py
```

A API ficará disponível em:

```
http://localhost:8080
```

---

## 🔁 Exemplo de Endpoint

### Requisição

```
GET /people/1
```

### Fluxo

1. API Pod recebe a requisição
2. Encaminha para:

   ```
   https://swapi.dev/api/people/1/
   ```
3. Retorna o JSON original ao cliente

---

## ☁️ Deploy no Google Cloud

### Opções recomendadas

* **Cloud Run** (mais simples)
* **Compute Engine** (mais controle)

> O código foi pensado para funcionar bem com Cloud Run.

---

## 🛡 Integração com Apigee

Enquanto o Apigee é configurado, o backend pode ser testado diretamente.

Depois, no Apigee:

1. Criar um **API Proxy**
2. Target Endpoint apontando para o serviço no Cloud Run
3. Definir base path (ex: `/swapi`)
4. Aplicar políticas:

   * Quota
   * Spike Arrest
   * Security

---

## 🧪 Testes Manuais

```bash
curl http://localhost:8080/people/1
```

Ou, via Apigee:

```bash
curl https://SEU-DOMINIO-APIGEE/swapi/people/1
```

---


## 🧠 Objetivo do Projeto

Este projeto não é apenas funcional — ele foi criado para:

* Demonstrar **arquitetura real de APIs**
* Servir como **base de estudo para Apigee**
* Evoluir para algo profissional

---

## ✍️ Autor

**Bruno Ramos**
Backend | APIs | Cloud | Python
https://www.linkedin.com/in/ramosbruno90/

