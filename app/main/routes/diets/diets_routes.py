from http import HTTPStatus
from fastapi import Response

from app.domain.usecases import CreateDietParams, CreateDietResponse
from app.main.adapters import fastapi_adapter
from app.main.factories import create_diet_factory

from main import app

TAG = ['Diets']

@app.post(
    '/diet/create-diet',
    responses= {
        HTTPStatus.CREATED.value: {
            'description': 'User created',
            'model': CreateDietResponse
        }
    },
    status_code=HTTPStatus.CREATED,
    tags=TAG
)
def create_diet(params: CreateDietParams, response: Response):
    request = {
        'body': params,
        'headers': None,
        'query': None
    }
    result = fastapi_adapter(request, create_diet_factory())

    response.status_code = result.status_code

    if result.body:
        return result.body

    return response
