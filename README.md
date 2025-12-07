📘 Workout API – Desafio DIO

Este repositório contém a implementação completa do desafio final proposto pela Digital Innovation One (DIO) no módulo de FastAPI, baseado no projeto original disponibilizado pelo expert.

O objetivo foi replicar e aprimorar a Workout API, adicionando funcionalidades profissionais, tratamento de erros, paginação e filtros avançados.

🚀 Tecnologias utilizadas

Python 3.11

FastAPI

SQLAlchemy 2.0

SQLite

Pydantic v2

Uvicorn

fastapi-pagination

🎯 Objetivos atendidos (Checklist oficial da DIO)
✔️ 1. Adicionar Query Parameters no endpoint de atletas

nome

cpf

✔️ 2. Customizar resposta do GET ALL /atletas

Retornar apenas:

nome

centro_treinamento

categoria

✔️ 3. Manipular exceção de integridade (IntegrityError)

Capturar erro de CPF duplicado

Retornar:

Status: 303

Mensagem: "Já existe um atleta cadastrado com o cpf: X"

✔️ 4. Adicionar paginação (limit/offset)

Implementado com fastapi-pagination

Estrutura padrão:

items

limit

offset

total

✔️ Todos os critérios do desafio foram cumpridos.

📂 Estrutura do projeto
app/
│── database.py
│── main.py
│── models.py
│── schemas.py
│
└── routers/
    │── atleta.py
    │── categoria.py
    └── centro_treinamento.py

⚙️ Como executar o projeto
1️⃣ Clonar o repositório
git clone https://github.com/SEU_USUARIO/workout_api_desafio.git
cd workout_api_desafio

2️⃣ Criar e ativar o ambiente virtual
python -m venv venv


Windows:

.\venv\Scripts\activate


Linux/Mac:

source venv/bin/activate

3️⃣ Instalar as dependências
pip install -r requirements.txt

4️⃣ Rodar o servidor
uvicorn app.main:app --reload


API rodando em:

http://127.0.0.1:8000


Documentação Swagger:

http://127.0.0.1:8000/docs

🧪 Testando os endpoints
🏋️ Atletas
➤ Criar atleta

POST /atletas/

Exemplo:

{
  "nome": "João da Silva",
  "cpf": "12345678901",
  "idade": 25,
  "peso": 75.5,
  "altura": 1.80,
  "centro_treinamento_id": 1,
  "categoria_id": 1
}

➤ Listar atletas (com paginação + filtros)

GET /atletas/?limit=10&offset=0&nome=joao

Response customizada:

{
  "items": [
    {
      "nome": "João da Silva",
      "centro_treinamento": "CT DIO Sports",
      "categoria": "Peso leve"
    }
  ],
  "limit": 10,
  "offset": 0,
  "total": 1
}

➤ CPF duplicado (erro customizado)
{
  "detail": "Já existe um atleta cadastrado com o cpf: 12345678901"
}


Status: 303

🏆 Diferenciais implementados

Estrutura modular e organizada (routers separados).

Paginação estruturada seguindo boas práticas.

Joins otimizados com joinedload.

Respostas enxutas e orientadas ao modelo solicitado.

Tratamento profissional de erros de integridade.

📎 Referência

Repositório original da DIO:
https://github.com/digitalinnovationone/workout_api
