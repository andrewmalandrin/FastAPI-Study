from app.services.contracts import ProductsData
from typing import List

def mount_products_data(file: List) -> ProductsData:
    products = []

    for row in file:
        if row[1].isnumeric():
            product = {
                'name': row[0],
                'portion': int(row[1]),
                'portion_unity':row[2],
                'carbohidrates': float(row[3]),
                'proteins': float(row[4]),
                'fat': float(row[5]),
                'saturated_fat': float(row[6])
            }
            products.append(product)

    return products
