from array import array
from http import HTTPStatus
from typing import Optional
from urllib.request import Request
from fastapi import FastAPI, Response
from pydantic import Json
from app.models.basemodel.requests import Product_Base
from app.file_mgmt import load_file
from app.file_mgmt import update_file

app = FastAPI(
    title='FoodFacts',
    version='1.0.0'
)

@app.get('/')
def index():
    return 'Welcome to the FoodFacts Brazil project by Andrew Malandrin'

@app.get('/products/{product_name}', responses={
        HTTPStatus.NOT_FOUND.value: {
            'description': 'Product not found'
        }
    })
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

@app.post('/products/new-product')
def create_new_product(request: Product_Base):
    update_file.create_line(request)

    return({'data':'Produto adicionado com sucesso'}, {'produto':request.name})


