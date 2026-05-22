# 📚 CRUD JSON Students

> Um CRUD simples em Python focado em organização de código, modularização e persistência de dados com JSON.

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-green)
![Rich](https://img.shields.io/badge/Rich-15.0.0-purple)
![JSON](https://img.shields.io/badge/database-JSON-orange)

---

# 📖 Visão Geral

Este projeto foi desenvolvido com o objetivo de consolidar fundamentos importantes da programação utilizando Python puro.

O sistema funciona como um CRUD de alunos, permitindo:

- Criar alunos
- Listar alunos
- Atualizar alunos
- Deletar alunos

Os dados são persistidos localmente em um arquivo JSON, simulando uma pequena camada de banco de dados para fins de estudo.

O foco principal do projeto NÃO foi criar uma arquitetura complexa, mas sim:

- Melhorar organização de código
- Praticar modularização
- Separar responsabilidades
- Trabalhar fluxo de aplicação
- Desenvolver raciocínio lógico
- Evoluir boas práticas

---

# 🛠️ Stack Técnica

| Tecnologia | Versão |
|---|---|
| Python | 3.12+ |
| Rich | 15.0.0 |
| Pygments | 2.20.0 |
| markdown-it-py | 4.2.0 |
| mdurl | 0.1.2 |
| JSON | Nativo do Python |

---

# 🏗️ Estrutura do Projeto

```bash
crud-json/
│
├── config/
│   └── constants.py
│
├── core/
│   ├── flow.py
│   └── service.py
│
├── ui/
│   └── msg.py
│
├── main.py
├── alunos.json
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# ⚙️ Arquitetura e Organização

O projeto foi dividido em módulos simples com responsabilidades específicas.

---

## `main.py`

Responsável pelo ponto de entrada da aplicação.

Controla:

- Loop principal
- Menu interativo
- Fluxo de execução
- Encerramento da aplicação

---

## `core/flow.py`

Responsável pelo fluxo principal do sistema.

Funções:

- Comunicação entre módulos
- Controle das funcionalidades
- Fluxo das operações CRUD
- Tratamento básico de respostas

---

## `core/service.py`

Camada responsável pela persistência e manipulação de dados.

Responsabilidades:

- Leitura de JSON
- Escrita em JSON
- Atualização de dados
- Exclusão de registros
- Manipulação de arquivos

---

## `ui/msg.py`

Responsável pelo feedback visual do terminal utilizando Rich.

Inclui:

- Mensagens coloridas
- Feedback de erro
- Feedback de sucesso
- Formatação visual

---

## `config/constants.py`

Centraliza constantes e mensagens utilizadas pelo sistema.

---

# ✨ Funcionalidades

## 👤 Cadastro de Alunos

Permite cadastrar alunos contendo:

- Nome
- Idade

---

## 📋 Listagem de Alunos

Exibe todos os alunos cadastrados em terminal formatado.

Exemplo:

```bash
ID - NOME - IDADE
1 - Enzo - 18
2 - Clara - 17
```

---

## ✏️ Atualização de Dados

Permite atualizar alunos utilizando o ID exibido na listagem.

---

## ❌ Remoção de Alunos

Permite deletar alunos cadastrados através do ID.

---

## 🎨 Feedback Visual

A aplicação utiliza Rich para melhorar experiência no terminal:

- Mensagens coloridas
- Melhor legibilidade
- Feedbacks organizados

---

# 🚀 Guia de Instalação e Execução

## Pré-requisitos

- Python 3.12+
- Git

---

# Passo 1 — Clonar o repositório

```bash
git clone <url-do-repositorio>
```

---

# Passo 2 — Entrar na pasta do projeto

```bash
cd crud-json
```

---

# Passo 3 — Criar ambiente virtual

## Linux / macOS

```bash
python3 -m venv venv
```

## Windows

```bash
python -m venv venv
```

---

# Passo 4 — Ativar ambiente virtual

## Linux / macOS

```bash
source venv/bin/activate
```

## Windows

```bash
venv\Scripts\activate
```

---

# Passo 5 — Instalar dependências

```bash
pip install -r requirements.txt
```

---

# Passo 6 — Executar aplicação

```bash
python main.py
```

---

# 💾 Persistência de Dados

Os dados são armazenados localmente em um arquivo JSON.

Exemplo:

```json
[
    {
        "name": "Enzo",
        "age": 18
    },
    {
        "name": "Clara",
        "age": 17
    }
]
```

---

# 🎯 Objetivos de Aprendizado

Este projeto foi criado para praticar:

- Modularização
- Separação de responsabilidades
- Estruturação de projetos
- Manipulação de arquivos
- JSON
- Tratamento de erros
- Organização de código
- Fluxo de aplicação
- Refatoração
- Legibilidade

---

# 🔮 Melhorias Futuras

- Sistema de IDs reais
- Exceptions customizadas
- Persistência com banco de dados
- Uso de POO
- Melhor separação de camadas
- Testes automatizados
- Interface gráfica
- API REST

---

# 📌 Observações

Este projeto possui foco educacional e foi desenvolvido visando evolução prática em Python e lógica de programação.

A arquitetura foi mantida propositalmente simples para consolidar fundamentos antes de avançar para conceitos mais complexos.

---

# 👨‍💻 Autor

Desenvolvido por Enzo Peralva para fins de estudo e evolução prática em programação.