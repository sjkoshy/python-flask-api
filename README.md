# Seinfeld API

This API is built with Python, Flask, and PostgreSQL.

## Installation

Run the following prompts in your terminal:

```
pip3 install pipenv
pipenv install
pipenv shell
python3 app.py
```

## Endpoints

| HTTP Method | API Endpoint       | Description               |
| ----------- | ------------------ | ------------------------- |
| GET         | `/characters`      | Retrieves all characters  |
| GET         | `/characters/<id>` | Retrieves character by id |
| PUT         | `/characters/<id>` | Updates character by id   |
| POST        | `/characters`      | Creates new character     |
| DELETE      | `/characters/<id>` | Deletes character by id   |
