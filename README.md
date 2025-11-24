# People API

API desenvolvida em **Django REST Framework + MongoDB** para gerenciar o cadastro de pessoas.

## 🚀 Funcionalidades
- Cadastro de pessoas com os campos:
  - Nome
  - Sobrenome
  - Data de nascimento (formato `yyyy-mm-dd`)
  - CPF (único e válido)
- CRUD completo (Create, Read, Update, Delete)
- Paginação server-side (5 itens por página)
- Validação de CPF
- Exibição da idade calculada automaticamente a partir da data de nascimento
- Estrutura organizada (serializers, services, utils, tests)
- Tratamento de erros e mensagens claras (ex: CPF inválido, duplicado, campos faltantes)

## ✨ Diferenciais
- Docker do ambiente
- Testes básicos com DRF
- Commits organizados
- Estrutura de pastas limpa
- Mensagens de erro amigáveis

---

## 📂 Estrutura de pastas
'''
backend/
├─ .venv/ 
├─ .env
├─ manage.py
├─ people_api/
│  ├─ __init__.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  ├─ asgi.py
│  └─ pagination.py
└─ people/
   ├─ __init__.py
   ├─ admin.py
   ├─ apps.py
   ├─ models.py
   ├─ serializers.py 
   ├─ views.py
   ├─ urls.py
   ├─ services.py
   ├─ utils.py
   ├─ exceptions.py
   └─ migrations/
      └─ __init__.py
---

## ⚙️ Instalação

### 1. Clonar o repositório
```bash
git clone https://github.com/seuusuario/people_api.git
cd people_api


2. Criar ambiente virtual
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows


3. Instalar dependências
pip install -r requirements.txt


4. Configurar MongoDB
- Local: mongodb://localhost:27017/people_db
- Docker: mongodb://mongo:27017/people_db
5. Rodar servidor
python manage.py runserver



🐳 Docker
Dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


docker-compose.yml
version: "3.9"
services:
  mongo:
    image: mongo:6
    ports:
      - "27017:27017"
    volumes:
      - mongo_data:/data/db
  web:
    build: .
    command: sh -c "python manage.py runserver 0.0.0.0:8000"
    ports:
      - "8000:8000"
    depends_on:
      - mongo
    environment:
      - MONGODB_URI=mongodb://mongo:27017/people_db
volumes:
  mongo_data:



🔗 Endpoints
Listar pessoas (paginação 5 por página)
GET /api/people/


Detalhar pessoa
GET /api/people/{id}/


Criar pessoa
POST /api/people/
Content-Type: application/json

{
  "first_name": "Joao",
  "last_name": "Silva",
  "birth_date": "1990-05-10",
  "cpf": "52998224725"
}


Atualizar pessoa
PATCH /api/people/{id}/
Content-Type: application/json

{
  "last_name": "Souza"
}


Deletar pessoa
DELETE /api/people/{id}/



📊 Exemplos de respostas
Sucesso (201 Created)
{
  "id": "6923ad3258fff37836909c37",
  "first_name": "Joao",
  "last_name": "Silva",
  "birth_date": "1990-05-10",
  "cpf": "52998224725",
  "age": 35
}


Erro CPF inválido (400 Bad Request)
{
  "cpf": ["CPF inválido"]
}


Erro CPF duplicado (400 Bad Request)
{
  "cpf": ["CPF já existe"]
}



🧪 Testes
Rodar testes com:
python manage.py test app_people


Testes cobrem:
- Criar pessoa válida
- Criar pessoa com CPF inválido
- Criar pessoa com CPF duplicado
- Paginação (5 itens por página)
