from typing import List

def mount_meals_data(file: List) -> List:
    meals = []

    for row in file:
        if len(row) > 0:
            if row[0].isnumeric():
                meal = {
                    'id': int(row[0]),
                    'diet_id': int(row[1]),
                    'description': row[2]
                }
                meals.append(meal)
    print("Products data: ", meals)
    return meals
