from http import HTTPStatus
from fastapi import Response

from app.domain.usecases import CreateDietParams, CreateDietResponse, GetDietResponse, GetDietParams
from app.main.adapters import fastapi_adapter
from app.main.factories import create_diet_factory, get_diet_factory

from main import app

TAG = ['Diets']

@app.post(
    '/diet/create',
    responses = {
        HTTPStatus.CREATED.value: {
            'description': 'User created',
            'model': CreateDietResponse
        }
    },
    status_code = HTTPStatus.CREATED,
    tags = TAG
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


@app.get(
    '/diet/{diet_id}',
    responses = {
        HTTPStatus.OK.value: {
            'description': 'Diet recovered successfully',
            'model': GetDietResponse
        },
        HTTPStatus.NOT_FOUND.value: {
            'description': 'Diet, meal or product not found'
        }
    },
    status_code = HTTPStatus.OK,
    tags = TAG
)
def get_diet(diet_id: int, response: Response):
    params = GetDietParams(
        id=diet_id
    )

    request = {
        'body': params,
        'headers': None,
        'query': None
    }

    result = fastapi_adapter(request, get_diet_factory())

    response.status_code = result.status_code

    if result.body:
        return result.body

    return response
