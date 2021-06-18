# Playing with FastAPI
This project scaffolded by Ivan Semernyakov beatuminflow@gmail.com

## Features
- **FastAPI** - is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints (includes Starlette and Pydantic)
- **Uvicorn** - lightning-fast ASGI server implementation, using uvloop and httptools
- **Pipenv** - is a python development workflow for humans
- **API docs** - automatic interactive API documentation provided by Swagger UI or ReDoc and OpenApi specification

## Installation
```
mkdir project
cd project
git clone https://github.com/beatum/extestcase.git
cd extestcase
pip install pipenv
pipenv install
pipenv shell
# check that`s all installed
pipenv graph

```

## Run the server
```
python main.py
```

## Useful links

* http://127.0.0.1:8000 - Root (store information about fake db in json format)
* http://127.0.0.1:8000/api/docs - SwaggerUi
* http://127.0.0.1:8000/redoc - ReDocUI

## API

#### POST http://127.0.0.1:8000/api/create
Create new item in the json format

Example Value
```
{
  "js": {}
}
```
#### GET http://127.0.0.1:8000/api/read
Return all items from db
```
curl -X 'GET' \
  'http://127.0.0.1:8000/api/read' \
  -H 'accept: application/json'
```
#### GET http://127.0.0.1:8000/api/read?sum=2
The optional parameter 'sum(integer)' indicates the number of records that will be returned,
```
curl -X 'GET' \
  'http://127.0.0.1:8000/api/read?sum=2' \
  -H 'accept: application/json'
```
