# Executando Tarefas Automatizadas com Lambda Function e S3

> Projeto desenvolvido durante o **Bootcamp de Cloud com AWS da DIO**, com o objetivo de construir uma arquitetura serverless em ambiente local utilizando o **LocalStack** para simular serviços da AWS.

## 📖 Descrição

Neste projeto foi desenvolvida uma solução para automatizar o processamento de notas fiscais utilizando serviços da AWS em ambiente local. A aplicação integra **Amazon S3**, **AWS Lambda**, **Amazon DynamoDB** e **Amazon API Gateway**, permitindo praticar a criação e integração desses serviços por meio da **AWS CLI** e do **Docker**.

---

## 🎯 Objetivos

- Configurar um ambiente AWS local utilizando o LocalStack;
- Criar um bucket no Amazon S3;
- Criar uma tabela no Amazon DynamoDB;
- Desenvolver uma função AWS Lambda em Python;
- Automatizar o processamento de arquivos enviados ao S3;
- Configurar uma API REST utilizando o Amazon API Gateway;
- Integrar os serviços utilizando a AWS CLI.

---

## 🛠 Tecnologias Utilizadas

- AWS CLI
- LocalStack
- Docker Desktop
- Python
- AWS Lambda
- Amazon S3
- Amazon DynamoDB
- Amazon API Gateway

---

## 📂 Estrutura do Projeto

```
├── grava_db.py
├── lambda_function.zip
├── nota_teste.json
├── payload.json
├── notification_roles.json
├── README.md
└── images/
```

---

## 🏗️ Arquitetura da Solução

A arquitetura desenvolvida durante o desafio pode ser visualizada no diagrama abaixo.

![Diagrama da Arquitetura](images/diagrama-estrutura.png)

---

## 🚀 Etapas Desenvolvidas

- Configuração do ambiente com Docker Desktop e LocalStack;
- Configuração da AWS CLI;
- Criação do bucket Amazon S3;
- Criação da tabela Amazon DynamoDB;
- Desenvolvimento da função AWS Lambda em Python;
- Configuração do gatilho (trigger) do S3;
- Criação da API REST utilizando o Amazon API Gateway;
- Configuração dos métodos GET e POST;
- Integração entre API Gateway e AWS Lambda;
- Deploy da API para testes locais.

---

## 📸 Evidências

Adicionar capturas de tela de:

- Docker Desktop
- LocalStack em execução
- Bucket S3 criado
- DynamoDB criado
- Lambda criada
- Trigger do S3
- API Gateway configurada
- Deploy realizado
- Testes executados

---

## 📚 Conclusão

O desenvolvimento deste projeto proporcionou uma experiência prática na construção de uma arquitetura **serverless** utilizando serviços da AWS em ambiente local por meio do LocalStack. Durante o desafio foi possível compreender melhor a integração entre **Amazon S3**, **AWS Lambda**, **Amazon DynamoDB** e **Amazon API Gateway**, além de praticar a criação e o gerenciamento desses recursos utilizando a **AWS CLI**.

A atividade também reforçou conceitos importantes sobre automação de infraestrutura, processamento de eventos e integração entre serviços em aplicações baseadas em nuvem.

---

## 👩‍💻 Autora

**Talita**
