from app.services.contracts import ProductsData
from typing import List

def mount_products_data(file: List) -> ProductsData:
    products = []

    for row in file:
        if len(row) > 0:
            if row[0].isnumeric():
                product = {
                    'id': int(row[0]),
                    'name': row[1],
                    'portion': int(row[2]),
                    'portion_unity':row[3],
                    'carbohidrates': float(row[4]),
                    'proteins': float(row[5]),
                    'fat': float(row[6]),
                    'saturated_fat': float(row[7])
                }
                products.append(product)
    print("Products data: ", products)
    return products
