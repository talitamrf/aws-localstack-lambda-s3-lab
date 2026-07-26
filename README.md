# Executando Tarefas Automatizadas com Lambda Function e S3

> Projeto desenvolvido durante o **Bootcamp GFT - Fundamentos de Cloud com AWS da DIO**, utilizando o **LocalStack** para simular serviços da AWS em ambiente local.

## 📖 Descrição

Neste projeto foi desenvolvida uma arquitetura serverless para processar notas fiscais em formato JSON.

A solução utiliza:

- Amazon S3
- AWS Lambda
- Amazon DynamoDB
- Amazon API Gateway
- LocalStack
- AWS CLI
- Docker

O projeto possui dois fluxos principais:

1. O envio de um arquivo JSON ao S3 dispara automaticamente a função Lambda, que grava as notas no DynamoDB.
2. A API Gateway permite cadastrar novas notas com o método POST e consultar os registros com o método GET.

---

## 🏗️ Arquitetura

![Diagrama da arquitetura](imagens/diagrama-estrutura.png)

---
## 🛠️ Tecnologias e serviços utilizados

- AWS CLI
- LocalStack
- Docker Desktop
- PowerShell
- Python
- AWS Lambda
- Amazon S3
- Amazon DynamoDB
- Amazon API Gateway
---

## 📂 Estrutura do Projeto
---
.
├── grava_db.py
├── gerar_dados.py
├── lambda_function.zip
├── notification_roles.json
├── notas_fiscais_2025.json
├── README.md
│
├── docs/
│   └── logs-localstack.txt
│
└── imagens/
    ├── diagrama-estrutura.png
    ├── 01-configuracao-trigger-s3.png
    ├── 02-integracao-api-post-get.png
    ├── 03-dynamodb-notas-cadastradas.png
    ├── 04-dynamodb-notas-cadastradas2.png
    ├── 05-testes-api-get-post.png
    ├── 06-lambda-localstack.png
    ├── 07-api-gateway-detalhes.png
    └── 08-api-gateway-metodos.png
---

## 🚀 Etapas Desenvolvidas

- Preparação do ambiente com Docker, LocalStack e AWS CLI;
- Criação do bucket S3 e da tabela no DynamoDB;
- Desenvolvimento e configuração da função Lambda;
- Configuração do trigger do S3 para executar a Lambda;
- Envio e processamento do arquivo JSON;
- Criação da API REST no API Gateway;
- Configuração dos métodos GET e POST;
- Integração da API com a Lambda;
- Testes pelo PowerShell e validação pelos logs do LocalStack.
