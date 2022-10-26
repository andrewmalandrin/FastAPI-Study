from enum import Enum

class PathsEnum(str, Enum):
    '''Paths enums class'''
    USERS_PATH = './app/infra/data/tsf/users.tsv'
    PRODUCTS_PATH = './app/infra/data/tsf/products.tsv'
    DIETS_PATH = './app/infra/data/tsf/diets.tsv'
    MEALS_PATH = './app/infra/data/tsf/meals.tsv'
    MEAL_PRODUCTS_PATH = './app/infra/data/tsf/meal_products.tsv'
