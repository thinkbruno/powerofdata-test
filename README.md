# API PowerOfData – SWAPI Proxy com Apigee

## 📌 Visão Geral

Esta aplicação implementa uma **API REST em Python** que consome dados da **SWAPI (Star Wars API)** e os expõe de forma estruturada, segura e escalável utilizando **Google Cloud Platform (GCP)** e **Apigee X** como API Gateway.

O projeto foi desenvolvido como solução de teste técnico, demonstrando conhecimentos práticos em **API Management, Cloud Functions, segurança, filtros de dados, testes automatizados e documentação profissional**.

---

## 🏗️ Arquitetura da Solução

```
Cliente (curl / Postman / Browser)
        ↓
Apigee X (API Gateway)
  - API Key
  - Quota
  - HTTPS / SSL
        ↓
Cloud Function (Python)
        ↓
SWAPI (https://swapi.dev)
```

### Componentes

* **Apigee X (Evaluation)**

  * Exposição pública da API
  * Autenticação via API Key
  * Rate limit (Quota)
  * Observabilidade e controle de acesso

* **Cloud Function (Python 3.12)**

  * Proxy inteligente da SWAPI
  * Filtros, ordenação e paginação
  * Código desacoplado e testável

* **SWAPI**

  * Fonte oficial dos dados de Star Wars

---

🌐 API Pública (Apigee)

A API está publicada e exposta via Apigee X (API Gateway), com HTTPS e autenticação por API Key.

Base URL
https://<SEU_IP>.nip.io/swapi

🔐 Autenticação: o acesso é protegido por API Key (Apigee).
A chave pode ser fornecida separadamente para fins de avaliação.

---

## 🚀 Endpoint Principal

```
GET /swapi
```

### Parâmetros de Query

| Parâmetro | Tipo   | Obrigatório | Descrição                              |
| --------- | ------ | ----------- | -------------------------------------- |
| resource  | string | ✅           | people, films, planets, starships      |
| name      | string | ❌           | Filtro por nome ou título              |
| sort      | string | ❌           | Campo para ordenação (`name`, `-name`) |
| page      | int    | ❌           | Página (default: 1)                    |
| page_size | int    | ❌           | Itens por página (default: 10)         |
| apikey    | string | ✅           | API Key gerada no Apigee               |

### Exemplo de Uso

```bash
curl "https://<SEU_IP>.nip.io/swapi?resource=people&name=Luke&apikey=SUA_API_KEY"
```

---

## 🔐 Segurança

* Autenticação via **API Key (Apigee)**
* HTTPS com certificado gerenciado pelo GCP
* Controle de quota por aplicação

---

## 🧪 Testes

Testes unitários implementados com **pytest**, cobrindo:

* Ordenação de resultados
* Paginação
* Validação de parâmetros

Executar localmente:

```bash
pytest
```

---

## 📂 Estrutura do Projeto

```
.
├── main.py               # Entry point da Cloud Function
├── app/
│   ├── __init__.py
│   └── swapi.py          # Lógica principal da API
├── tests/
│   └── test_swapi.py     # Testes unitários
├── requirements.txt
├── openapi.yaml          # Documentação OpenAPI
└── README.md
```

---

## 📄 OpenAPI / Swagger

O arquivo `openapi.yaml` descreve completamente os endpoints, parâmetros e respostas da API, podendo ser importado em ferramentas como **Swagger UI**, **Postman** ou diretamente no **Apigee**.

---

## ☁️ Deploy no GCP (Resumo)

1. Deploy da Cloud Function (Python 3.12)
2. Criação do Apigee X (Evaluation)
3. Criação do API Proxy apontando para a Cloud Function
4. Configuração de API Product, Developer e App
5. Geração da API Key

---

## 🎯 Diferenciais Técnicos

* Uso real de **Apigee X** (não mock)
* Arquitetura cloud-native
* Código limpo e testável
* Segurança aplicada no gateway
* Documentação clara e reutilizável

---

## 👤 Autor

**Bruno Ramos**

Projeto desenvolvido para fins de avaliação técnica.

https://www.linkedin.com/in/ramosbruno90/

