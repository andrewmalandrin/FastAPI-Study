from http import HTTPStatus
from fastapi import Response

from app.domain.usecases.users import GetUsersResponse, GetUserByIdResponse, GetUserByIdParams, CreateUserParams, \
    CreateUserResponse, UpdateUserParams, UpdateUserResponse, DeleteUserParams, DeleteUserResponse
from app.main.factories import get_user_by_id_factory, get_users_factory, create_user_factory, update_user_factory, delete_user_factory
from app.main.adapters import fastapi_adapter

from main import app

TAG = ['Users']


@app.get(
    '/users/{user_id}',
    responses={
        HTTPStatus.OK.value: {
            'description' : 'Get user by ID',
            'model' : GetUserByIdResponse
        },
        HTTPStatus.NOT_FOUND.value:{
            'description' : 'User not found'
        }
    },
    tags=TAG
)
def get_user_by_id(user_id: int, response: Response):
    request = {
        'body' : GetUserByIdParams(
            id=user_id
        ),
        'headers' : None,
        'query' : None
    }
    result = fastapi_adapter(request, get_user_by_id_factory())

    response.status_code = result.status_code

    if result.body:
        return result.body
    return response

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

@app.post(
    '/users/create',
    responses={
        HTTPStatus.CREATED.value: {
            'description' : 'Create user endpoint',
            'model' : CreateUserResponse
        }
    },
    tags=TAG
)
def create_user(params: CreateUserParams, response: Response):
    request = {
        'body': params,
        'headers': None,
        'query' : None
    }

    result = fastapi_adapter(request, create_user_factory())

    response.status_code = result.status_code

    if result.body:
        return result.body
    return response

@app.put(
    '/users/update',
    responses={
        HTTPStatus.ACCEPTED.value: {
            'description' : 'Change accepted',
            'model' : UpdateUserResponse
        },
        HTTPStatus.NOT_FOUND.value: {
            'description' : 'User not found'
        }
    },
    status_code=HTTPStatus.ACCEPTED,
    tags=TAG
)
def update_user(params: UpdateUserParams, response: Response):
    request = {
        'body': params,
        'headers': None,
        'query' : None
    }

    result = fastapi_adapter(request, update_user_factory())

    response.status_code = result.status_code

    if result.body:
        return result.body
    return response

@app.delete(
    '/users/delete-user/{user_id}',
    responses={
        HTTPStatus.OK.value: {
            'description': 'User delete',
            'model': DeleteUserResponse
        },
        HTTPStatus.NOT_FOUND.value: {
            'description': 'User not found'
        }
    },
    status_code=HTTPStatus.OK,
    tags=TAG
    )
def delete_user(user_id: int, response: Response):

    params = DeleteUserParams(
        id=user_id
    )

    request = {
        'body': params,
        'headers': None,
        'query': None
    }

    result = fastapi_adapter(request, delete_user_factory())

    response.status_code = result.status_code

    if result.body:
        return result.body
    return response
