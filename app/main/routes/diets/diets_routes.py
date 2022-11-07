from http import HTTPStatus
from fastapi import Response

from app.domain.usecases import CreateDietParams, CreateDietResponse, GetDietResponse, GetDietParams, UpdateDietParams,\
    UpdateDietResponse, UpdateMealResponse, UpdateMealParams, UpdateMealProductParams, UpdateMealProductResponse,\
        DeleteMealParams, DeleteMealProductParams, DeleteMealProductResponse, CreateMealParams, CreateMealResponse
from app.main.adapters import fastapi_adapter
from app.main.factories import create_diet_factory, get_diet_factory, update_diet_factory, update_meal_factory,\
    update_meal_product_factory, delete_meal_factory, delete_meal_product_factory, create_meal_factory

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

@app.put(
    '/diet/update',
    responses= {
        HTTPStatus.ACCEPTED.value: {
            'description': 'Change accepted',
            'model': UpdateDietResponse
        }
    },
    status_code=HTTPStatus.ACCEPTED,
    tags=TAG
)
def update_diet(params: UpdateDietParams, response: Response):
    request = {
        'body': params,
        'headers': None,
        'query': None
    }
    result = fastapi_adapter(request, update_diet_factory())

    response.status_code = result.status_code

    if result.body:
        return result.body

    return response

@app.post(
    '/meal/create',
    responses= {
        HTTPStatus.ACCEPTED.value: {
            'description': 'Meal created',
            'model': CreateMealResponse
        },
        HTTPStatus.NOT_FOUND.value: {
            'description': 'Product not found'
        }
    },
    status_code=HTTPStatus.ACCEPTED,
    tags=TAG
)
def create_meal(params: CreateMealParams, response: Response):
    request = {
        'body': params,
        'headers': None,
        'query': None
    }

    result = fastapi_adapter(request, create_meal_factory())

    response.status_code = result.status_code

    if result.body:
        return result.body

    return response

@app.put(
    '/meal/update',
    responses = {
        HTTPStatus.ACCEPTED.value:{
            'description': 'Change accepted',
            'model': UpdateMealResponse
        },
        HTTPStatus.NOT_FOUND.value: {
            'description': 'Meal not found'
        }
    },
    status_code=HTTPStatus.ACCEPTED,
    tags=TAG
)
def update_meal(params: UpdateMealParams, response: Response):
    request = {
        'body': params,
        'headers': None,
        'query': None
    }
    result = fastapi_adapter(request, update_meal_factory())

    response.status_code = result.status_code

    if result.body:
        return result.body

    return response

@app.delete(
    '/meal/delete',
    responses={
        HTTPStatus.ACCEPTED.value: {
            'Description': 'Meal deleted successfully'
        },
        HTTPStatus.NOT_FOUND.value: {
            'description': 'Meal or meal product not found'
        }
    },
    status_code=HTTPStatus.ACCEPTED,
    tags=TAG
)
def delete_meal(params: DeleteMealParams, response: Response):
    request = {
        'body': params,
        'headers': None,
        'query': None
    }
    result = fastapi_adapter(request, delete_meal_factory())

    response.status_code = result.status_code

    if result.body:
        return result.body

    return response

@app.put(
    '/meal/product/update',
    responses= {
        HTTPStatus.ACCEPTED.value: {
            'description': 'Meal product change accepted',
            'model': UpdateMealProductResponse
        },
        HTTPStatus.NOT_FOUND.value: {
            'description': 'Meal product not found'
        }
    },
    status_code=HTTPStatus.ACCEPTED,
    tags=TAG
)
def update_meal_product(params: UpdateMealProductParams, response: Response):
    request = {
        'body': params,
        'headers': None,
        'query': None
    }
    result = fastapi_adapter(request, update_meal_product_factory())

    response.status_code = result.status_code

    if result.body:
        return result.body

    return response

@app.delete(
    '/meal/product/delete',
    responses={
        HTTPStatus.ACCEPTED.value: {
            'description': 'Meal product deleted successfully',
            'model': DeleteMealProductResponse
        },
        HTTPStatus.NOT_FOUND.value: {
            'description': 'Meal product not found'
        }
    },
    status_code=HTTPStatus.ACCEPTED,
    tags=TAG
)
def delete_meal_product(params: DeleteMealProductParams, response: Response):
    request = {
        'body': params,
        'headers': None,
        'query': None
    }
    result = fastapi_adapter(request, delete_meal_product_factory())

    response.status_code = result.status_code

    if result.body:
        return result.body

    return response
