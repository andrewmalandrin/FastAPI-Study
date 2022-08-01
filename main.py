from array import array
from collections import namedtuple
from fastapi import FastAPI
from pydantic import Json
from app.file_mgmt import load_file

app = FastAPI()

@app.get('/')
def index():
    return 'Welcome to the FastAPI training project from Andrew Malandrin'

@app.get('/products/{product_name}')
def get_product(product_name: str = ""):
    return load_file.get_product_by_name(product_name)

@app.get('/products')
def get_products() -> array:
    products = load_file.tsv_read_file()
    return products



# @app.get('/products/{item}')
# def get_products(item: str) -> object:
#     products = {
#         "menovo_computer": {
#             "name": "computer menovo",
#             "price": "250000"
#         },
#         "portair_keyboard": {
#             "name": "keyboard portair",
#             "price": "15000"
#         }
#     }

#     return products.get(item)

# @app.get('/products/{item}/{attribute}')
# def get_products_attribute(item, attribute: int = 0) -> Json:
#     products = {
#         "menovo_computer": {
#             "name": "computer menovo",
#             1: "250000"
#         },
#         "portair_keyboard": {
#             "name": "keyboard portair",
#             1: "15000"
#         }
#     }
#     print(type(attribute))
#     return products.get(item)[attribute]

