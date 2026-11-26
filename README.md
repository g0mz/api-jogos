# API de Jogos

Trabalho final de Programação para Internet (UENP). Projeto Django com uma API para uma coleção
pessoal de jogos e uma página que consome essa API com `fetch`: lista os jogos, cadastra novos,
marca/desmarca como zerado e exclui, sem recarregar a página.

Cada jogo tem: `titulo` (texto), `plataforma` (texto), `ano` (número) e `zerado` (verdadeiro/falso).

## Como rodar
1. python -m venv venv
2. venv\Scripts\activate
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py runserver

Depois acesse `http://127.0.0.1:8000/` (página) ou `http://127.0.0.1:8000/api/jogos/` (API).

No Linux ou macOS, troque o passo 2 por `source venv/bin/activate`.

## Admin
Usuário: admin
Senha: admin123

Acesse em `http://127.0.0.1:8000/admin/`.

## Dados de teste
Os registros de teste (3 jogos) e o usuário admin estão no banco `db.sqlite3`, enviado junto com o
repositório.

## Rotas da API

| Método | URL              | Descrição        | Respostas     |
|--------|------------------|------------------|---------------|
| GET    | /api/jogos/      | Lista os jogos   | 200           |
| POST   | /api/jogos/      | Cadastra um jogo | 201, 400      |
| GET    | /api/jogos/<id>/ | Busca um jogo    | 200, 404      |
| PUT    | /api/jogos/<id>/ | Altera um jogo   | 200, 400, 404 |
| DELETE | /api/jogos/<id>/ | Exclui um jogo   | 204, 404      |

No POST, os campos `titulo`, `plataforma` e `ano` são obrigatórios. Exemplo de corpo:

```json
{"titulo": "Celeste", "plataforma": "PC", "ano": 2018}
```
