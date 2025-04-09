# 🤖 Assistente Virtual Santander (IA Local)

## 🧾 Introdução

Este projeto demonstra o uso de uma **Inteligência Artificial personalizada** para atuar como **atendente virtual** focado exclusivamente nos interesses do **Banco Santander**. Utilizando uma IA local, treinada com instruções específicas, foi possível simular interações reais com clientes de forma eficaz, segura e privada.

## 🎯 Objetivo

A IA tem como propósito atender usuários em um chat, oferecendo informações úteis e relevantes sobre a empresa. O escopo está limitado a **dados públicos e institucionais** do Santander, e algumas das principais dúvidas tratadas são:

- Horário de atendimento;
- Funcionamento em feriados;
- Telefones de contato conforme a necessidade;
- Localização de agencias;
- Contratação de produtos/serviços;
- Abertura de conta / contratação de cartão;
- Aumento de limite;
- Informações públicas e institucionais;
- Entre outras questões relacionadas aos serviços da empresa;

> A IA **não responde** dúvidas fora desse contexto e orienta corretamente quando isso acontece.

## ⚙️ Tecnologias Utilizadas

| Tecnologia | Descrição |
|------------|-----------|
| 🐍 **Python** | Linguagem principal do projeto |
| 🤖 **Modelo de IA local** | Baseado em arquitetura compatível com OpenAI API (chat-style) |
| 📡 **API Local** | Utilizando LM Studio como servidor com endpoints compatíveis |
| 📦 `requests`, `json`, | Bibliotecas auxiliares para integração e configuração |

## 📌 Endpoints Utilizados
> **http://127.0.0.1:1234/v1/chat/completions**

## Estrutura do projeto
```
├── chatbot/
│   ├── prompts/
│   │   └── prompt-aprendizado-1-a.txt
│   ├── main.py
│   └── gitignore
├── README.md
└── requirements.txt
```

## Execução do Programa
1. Clonar o repositório: ```git clone https://github.com/KristoferBorges/ChatBOT-Santander.git```;
2. Instalar as bibliotecas ```pip install -r requirements.txt```;
3. Baixar a IA usada direto no LM Studio```nous-hermes-2-mistral-7b-dpo```;
4. Inserir o prompt usado ```ChatBot\prompts\prompt-aprendizado-1-a.txt```;
5. Execute a IA no seu localhost;
6. Execute o **main.py** usando ```python main.py```

### 🎯 Seguindo esses passos irá abrir uma janela para conversar com a IA.

# Desafios durante o desenvolvimento
## _Durante o processo não encontrei muitas barreiras, o complicado foi gerir o consumo de memória e GPU por conta do peso que as IAs rodando localmente acabam gerando, entretanto a parte mais difícil foi encontrar uma IA base e treinar com os dados da empresa. No final das contas ainda teve certa deficiência de velocidade por conta do tamanho do prompt e o consumo de memória._