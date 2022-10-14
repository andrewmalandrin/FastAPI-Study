from fastapi import FastAPI

app = FastAPI(
    title='FoodFacts',
    version='1.0.0'
)

@app.get('/', tags=['Index'])
def index():
    return 'Welcome to the FoodFacts Brazil project by Andrew Malandrin'


from app.main.routes import *
