from http import HTTPStatus
from typing import List, Optional
from fastapi import Response

from app.domain.usecases import GetProductParams, GetProductResponse, GetProductsResponse,\
     CreateProductParams, CreateProductResponse
from app.main.adapters import fastapi_adapter
from app.main.factories import get_product_factory, get_products_factory, create_product_factory
from main import app

TAG = ['Products']

@app.get('/products/{product_name}',
    responses={
        HTTPStatus.OK.value: {
            'description':'Product found',
            'model': GetProductResponse
        },
        HTTPStatus.NOT_FOUND.value: {
            'description': 'Product not found'
        }
    },
    tags=TAG
)
def get_product(response: Response, product_name: str = "", portion: Optional[int] = None):

    request = {
        'body': GetProductParams(name=product_name,
        portion=portion),
        'headers': None,
        'query': None
    }

    result = fastapi_adapter(request, get_product_factory())
    print('Response result: ', result)

    response.status_code = result.status_code

    if result.body:
        return result.body

    return response


@app.get('/products',
    responses={
        HTTPStatus.OK.value:{
            'description': 'Products entire list',
            'model': GetProductsResponse
        }
    },
    tags=TAG
)
def get_products(response: Response):
    request = {
        'body': None,
        'headers': None,
        'query': None
    }

    result = fastapi_adapter(request, get_products_factory())

    response.status_code = result.status_code

    if result.body:
        return result.body

    return response

@app.post('/products/new-product',
    responses={
        HTTPStatus.CREATED.value: {
            'description': 'Product created',
            'model': CreateProductResponse
        },
        HTTPStatus.BAD_REQUEST.value: {
            'description': 'Product creation failed'
            },
        HTTPStatus.UNPROCESSABLE_ENTITY.value: {
            'description':'Incorrect data type'
        }
    },
    tags=TAG
)
def create_new_product(params: CreateProductParams, response: Response):
    request = {
        'body': params,
        'headers': None,
        'query': None
    }
    result = fastapi_adapter(request, create_product_factory())

    response.status_code = result.status_code

    if result.body:
        return result.body

    return response
