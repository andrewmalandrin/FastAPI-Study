from http import HTTPStatus
from typing import List, Optional
from fastapi import Response

from app.domain.usecases.users import GetUsersResponse
from app.main.factories import get_users_factory
from app.main.adapters import fastapi_adapter

from main import app

TAG = ['Users']

@app.get(
    '/users',
    responses={
        HTTPStatus.OK.value: {
            'description' : 'Users entire list',
            'model' : GetUsersResponse
        }
    },
    tags=TAG
)
def get_users(response: Response):
    request = {
        'body' : None,
        'headers' : None,
        'query' : None
    }

    result = fastapi_adapter(request, get_users_factory())

    response.status_code = result.status_code

    if result.body:
        return result.body
    return response
