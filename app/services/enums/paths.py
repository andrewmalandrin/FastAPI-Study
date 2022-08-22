from enum import Enum

class PathsEnum(str, Enum):
    '''Paths enums class'''
    USERS_PATH = './data/tsf/users.csv'
    PRODUCTS_PATH = './data/tsf/products.csv'
