from enum import Enum

class PathsEnum(str, Enum):
    '''Paths enums class'''
    USERS_PATH = './app/infra/data/tsf/users.tsv'
    PRODUCTS_PATH = './app/infra/data/tsf/products.tsv'
