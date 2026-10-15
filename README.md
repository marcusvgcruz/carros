# 🚗 Carros — Inventário de Veículos com IA

![Django](https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini%20API-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

Plataforma web para cadastro e controle de inventário de veículos. Duas coisas
acontecem **sozinhas**: a descrição de venda do carro é gerada por **IA** no
momento do cadastro e o **inventário se atualiza a cada movimentação** — as duas
automações usam **Django Signals**, sem botão e sem rotina agendada.

---

## ✨ Destaques

**1. Descrição técnica gerada por IA no momento do save.**
Antes de gravar o carro, um `pre_save` verifica se o campo `bio` está vazio e, se
estiver, consulta a **API do Gemini** com marca, modelo e ano para gerar um texto
de venda. O prompt foi escrito para devolver um parágrafo corrido — sem emojis,
hashtags ou tópicos — em cerca de 250 caracteres, cabendo direto no cadastro.

**2. Inventário com histórico, não só com o número atual.**
A cada cadastro ou exclusão, um `post_save`/`post_delete` recalcula o total de
carros e o **valor patrimonial acumulado** (agregação `Sum` feita no banco) e grava
um novo registro em `CarInventory`. Como cada movimentação gera uma linha datada,
o histórico fica disponível para acompanhar a evolução do estoque.

**3. CRUD completo com fotos.**
Listagem com busca e paginação, cadastro com upload de imagem (Pillow), edição e
exclusão — com a marca associada por chave estrangeira protegida (`on_delete=PROTECT`),
evitando que um carro fique sem marca.

---

## 🔄 Fluxo automático (Django Signals)

```text
Car.pre_save    →  sem bio preenchida, gera a descrição com a API do Gemini
Car.post_save   →  recalcula o inventário e grava um novo snapshot
Car.post_delete →  recalcula o inventário e grava um novo snapshot
```

---

## 🗂️ Models

| Model | Campos principais |
|---|---|
| `Brand` | nome da marca |
| `Car` | modelo, marca (FK protegida), ano de fabricação, ano do modelo, placa, valor, foto e descrição (`bio`) |
| `CarInventory` | quantidade de carros, valor total e data do registro |

---

## 📁 Estrutura

```text
carros/
├── app/            # configuração (settings, urls, wsgi/asgi)
├── accounts/       # cadastro, login e autenticação
├── cars/           # CRUD de veículos e marcas, templates e signals
├── gemini_api/     # cliente de integração com a API do Gemini
├── media/          # fotos enviadas dos veículos
└── manage.py
```

---

## 🚀 Como rodar

```bash
git clone https://github.com/marcusvgcruz/carros.git
cd carros

python3 -m venv .venv
source .venv/bin/activate        # Windows: .\.venv\Scripts\Activate.ps1

pip install -r requirements.txt

# chave da API do Gemini (usada na geração automática das descrições)
echo "GEMINI_API_KEY=sua_chave_aqui" > .env

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

A aplicação sobe em `http://127.0.0.1:8000/`.

---

## 📄 Autor

**Marcus Cruz** — [GitHub](https://github.com/marcusvgcruz) · [LinkedIn](https://www.linkedin.com/in/marcusvgcruz)
