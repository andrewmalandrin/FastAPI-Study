from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return 'First Fast API App'

@app.get('/products')
def get_products():
    products = {
        "product1": {
            "name": "computer menovo",
            "price": "250000"
        },
        "product2": {
            "name": "keyboard portair",
            "price": "15000"
        }
    }
    return products