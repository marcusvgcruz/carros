# 🚗 Carros — Sistema de Gerenciamento e Inventário de Veículos

Sistema web completo desenvolvido em **Python** e **Django** para cadastro, controle de inventário e gerenciamento de veículos, marcas e usuários. O projeto conta com rotinas de automação via *Django Signals* e integração inteligente com a API da **OpenAI** para geração de descrições detalhadas dos carros cadastrados.

---

## 📌 Funcionalidades

- **Autenticação & Contas (`accounts`):**
  - Cadastro de novos usuários (`register`).
  - Login e autenticação segura com redirecionamento de permissões (`login`).
- **Gerenciamento de Veículos (`cars`):**
  - Listagem com busca, paginação e visualização em cards/galeria.
  - Cadastro de novos veículos com upload de fotos (`media/cars/`).
  - Atualização e exclusão de carros cadastrados (operações CRUD completas).
  - Associação com marcas (`Brand`), placa e ano de fabricação/modelo.
- **Inventário Automático (`CarInventory` + Signals):**
  - Rastreamento e cálculo em tempo real do total de veículos no estoque e valor patrimonial acumulado a cada cadastro ou exclusão via *Django Signals*.
- **Inteligência Artificial Integrada (`openai_api`):**
  - Geração automática da biografia/descrição técnica (`bio`) do veículo consumindo modelos da OpenAI.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.12+
- **Framework Web:** [Django 6](https://www.djangoproject.com/)
- **Banco de Dados:** SQLite (padrão de desenvolvimento)
- **Processamento de Imagens:** Pillow (PIL)
- **Integração de IA:** Gemini API
- **Arquitetura:** MVT (Model-View-Template) com formulários e Class-Based Views

---

## 📂 Estrutura do Projeto

```text
carros/
├── accounts/          # Autenticação de usuários, login e registro
├── app/               # Configurações globais (settings, urls, wsgi/asgi)
├── cars/              # CRUD de veículos, marcas, formulários, templates e signals
├── media/             # Uploads de fotos de veículos
├── openai_api/        # Cliente de integração com a API da OpenAI
├── db.sqlite3         # Banco de dados local
├── manage.py          # Utilitário de linha de comando do Django
└── requirements.txt   # Dependências do projeto
