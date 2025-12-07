# Workout API - Desafio DIO

Este projeto é uma versão simplificada do repositório oficial da DIO
[`digitalinnovationone/workout_api`](https://github.com/digitalinnovationone/workout_api),
com as adaptações solicitadas no desafio final.

## Tecnologias

- Python 3.11+
- FastAPI
- SQLAlchemy
- SQLite
- fastapi-pagination

## Como executar o projeto

```bash
# criar e ativar um ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# instalar dependências
pip install -r requirements.txt

# executar a API
uvicorn app.main:app --reload
```

A API ficará disponível em: `http://127.0.0.1:8000`

A documentação interativa (Swagger) estará em: `http://127.0.0.1:8000/docs`

## Endpoints principais

### Centros de Treinamento

- `POST /centros_treinamento/`
- `GET /centros_treinamento/`

### Categorias

- `POST /categorias/`
- `GET /categorias/`

### Atletas

- `POST /atletas/`
  - Trata `sqlalchemy.exc.IntegrityError` para CPF duplicado e retorna:
    - **status_code:** `303`
    - **detail:** `Já existe um atleta cadastrado com o cpf: x`

- `GET /atletas/`
  - Suporta **query parameters**:
    - `nome` (opcional)
    - `cpf` (opcional)
  - Usa paginação de **limit/offset** (fastapi-pagination).
  - Response **customizada** com apenas:
    - `nome`
    - `centro_treinamento`
    - `categoria`

- `GET /atletas/{atleta_id}`:
  - Retorna o atleta completo (incluindo CPF e relações).

## Exemplo de uso da paginação

```bash
GET /atletas/?limit=10&offset=0
GET /atletas/?nome=joao&limit=5&offset=5
GET /atletas/?cpf=12345678901&limit=1&offset=0
```

Bons estudos e bom código! 💪
