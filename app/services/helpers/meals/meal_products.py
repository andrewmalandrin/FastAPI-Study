from typing import List

def mount_meal_products_data(file: List) -> List:
    meals_products = []

    for row in file:
        if len(row) > 0:
            if row[0].isnumeric():
                meal_product = {
                    'id': int(row[0]),
                    'meal_id': int(row[1]),
                    'product_id': int(row[2]),
                    'portion': int(row[3])
                }
                meals_products.append(meal_product)
    print("Products data: ", meals_products)
    return meals_products
