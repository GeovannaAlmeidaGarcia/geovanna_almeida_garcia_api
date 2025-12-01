📘 API de Livraria – Django Rest Framework
API desenvolvida em Django Rest Framework, contendo os modelos Autor, Categoria e Livro, permitindo cadastro, listagem, filtros e operações completas de CRUD.

🚀 Como rodar o projeto
1. Criar e ativar ambiente virtual (Windows)
python -m venv env
env\Scripts\activate

2. Instalar dependências
pip install -r requirements.txt

3. Aplicar migrações
python manage.py migrate

4. Rodar o servidor
python manage.py runserver

Servidor rodará em:
👉 http://127.0.0.1:8000/

📌 Endpoints Principais
Autores
GET /api/autores/ – lista todos os autores
POST /api/autores/ – cadastra novo autor
GET /api/autores/{id}/ – detalhes
PUT/PATCH /api/autores/{id}/ – editar
DELETE /api/autores/{id}/ – deletar

Categorias
GET /api/categorias/ – lista todas as categorias
POST /api/categorias/ – cadastra nova categoria
GET /api/categorias/{id}/ – detalhes
PUT/PATCH /api/categorias/{id}/ – editar
DELETE /api/categorias/{id}/ – deletar

Livros
GET /api/livros/ – lista todos os livros
POST /api/livros/ – cadastra novo livro
GET /api/livros/{id}/ – detalhes
PUT/PATCH /api/livros/{id}/ – editar
DELETE /api/livros/{id}/ – deletar

🔍 Filtros disponíveis (na listagem de livros)
Filtrar por categoria
/api/livros/?categoria=1

Filtrar por disponibilidade
/api/livros/?disponivel=true

Filtrar por autor
/api/livros/?autor=2
