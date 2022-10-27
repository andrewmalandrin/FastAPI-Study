from app.services.contracts import ProductsData
from typing import List, Dict

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

def calculate_portion(portion: int, product: List) -> Dict:

    calculated_product = {}

    calculated_product['id'] = product['id']
    calculated_product['name'] = product['name']
    calculated_product['portion'] = portion
    calculated_product['portion_unity'] = product['portion_unity']
    calculated_product['carbohidrates'] = round((product['carbohidrates']/product['portion']) * portion, 2)
    calculated_product['proteins'] = round((product['proteins']/product['portion']) * portion, 2)
    calculated_product['fat'] = round((product['fat']/product['portion']) * portion, 2)
    calculated_product['saturated_fat'] = round((product['saturated_fat']/product['portion']) * portion, 2)

    return calculated_product
