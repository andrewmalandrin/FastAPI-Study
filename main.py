from array import array
from typing import Optional
from fastapi import FastAPI
from pydantic import Json
from app.file_mgmt import load_file

app = FastAPI()

@app.get('/')
def index():
    return 'Welcome to the FastAPI training project from Andrew Malandrin'

@app.get('/products/{product_name}')
def get_product(product_name: str = "", portion: Optional[int] = None):
    
    if portion == None:
        return load_file.get_product_by_name(product_name)
    else:
        try:
            product = load_file.get_product_by_name(product_name)
            product = load_file.calculate_by_portion(product, portion)
            
            return product
        except Exception as exception:
            print(exception)
            return exception

@app.get('/products')
def get_products() -> array:
    products = load_file.tsv_read_file()
    return products



