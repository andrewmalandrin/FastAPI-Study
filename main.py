from array import array
from http import HTTPStatus
from typing import Optional
from fastapi import FastAPI, Response, status, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import Json
from app.models.basemodel.requests import Product_Base
from app.file_mgmt import load_file
from app.file_mgmt import update_file

app = FastAPI(
    title='FoodFacts',
    version='1.0.0'
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail":'Incorrect data type, verify data sent in body', "body": exc.body}),
    )

@app.get('/')
def index():
    return 'Welcome to the FoodFacts Brazil project by Andrew Malandrin'

@app.get('/products/{product_name}', 
        responses={
        HTTPStatus.NOT_FOUND.value: {
            'description': 'Product not found'
            }
        }
    )
def get_product(response: Response, product_name: str = "", portion: Optional[int] = None):
    
    if portion == None: 
        try:

            return load_file.get_product_by_name(product_name)
        except Exception as exception:
            response.status_code = HTTPStatus.NOT_FOUND
            response.content = "nenhum registro encontrado"
            print("Response: ", response.content)
            return response
    else:
        try:
            product = load_file.get_product_by_name(product_name)
            product = load_file.calculate_by_portion(product, portion)
            
            return product

        except:
            
            response.status_code = HTTPStatus.NOT_FOUND
            response.content = "nenhum registro encontrado"
            print("Response: ", response.content)
            return response.content

@app.get('/products')
def get_products() -> array:
    products = load_file.tsv_read_file()
    return products

@app.post('/products/new-product', responses={
        HTTPStatus.BAD_REQUEST.value: {
            'description': 'Product creation failed'
            },
        HTTPStatus.UNPROCESSABLE_ENTITY.value: {
            'description':'Incorrect data type'
        }
        })
def create_new_product(request: Product_Base, response: Response):
    try:
        response = update_file.create_line(request)
    except:
        print('Entrou no except')
        response.status_code = 422
        response.content = 'Incorrect data type'
    return response
    #return({'data':'Produto adicionado com sucesso'}, {'produto':request.name})


