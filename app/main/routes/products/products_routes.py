from http import HTTPStatus
from typing import List, Optional
from fastapi import Response

from app.domain.usecases import GetProductParams, GetProductResponse, GetProductsResponse,\
     CreateProductParams, CreateProductResponse, UpdateProductParams, UpdateProductResponse,\
        DeleteProductResponse, DeleteProductParams
from app.main.adapters import fastapi_adapter
from app.main.factories import get_product_factory, get_products_factory, create_product_factory, update_product_factory,\
    delete_product_factory
from main import app

TAG = ['Products']

@app.get('/products/{product_id}',
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
def get_product(response: Response, product_id: str = "", portion: Optional[int] = None):

    request = {
        'body': GetProductParams(id=product_id,
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
    status_code=HTTPStatus.CREATED,
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

@app.put(
    '/products/update',
    responses={
        HTTPStatus.ACCEPTED.value: {
            'description': 'Product updated',
            'model': UpdateProductResponse
        }
    },
    status_code=HTTPStatus.ACCEPTED,
    tags=TAG
)
def update_product(params: UpdateProductParams, response: Response):
    request={
        'body': params,
        'headers': None,
        'query': None
    }
    result = fastapi_adapter(request, update_product_factory())

    response.status_code = result.status_code

    if result.body:
        return result.body

    return response

@app.delete(
    '/product/delete/{product_id}',
    responses={
        HTTPStatus.ACCEPTED.value: {
            'description': 'Product deleted',
            'model': DeleteProductResponse
        },
        HTTPStatus.NOT_FOUND.value: {
            'description': 'Product not found'
        }
    },
    status_code=HTTPStatus.ACCEPTED,
    tags=TAG
    )
def delete_product(product_id: int, response: Response):
    params = DeleteProductParams(
        id=product_id
    )
    
    request={
        'body': params,
        'headers': None,
        'query': None
    }
    result = fastapi_adapter(request, delete_product_factory())

    response.status_code = result.status_code

    if result.body:
        return result.body

    return response