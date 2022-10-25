from typing import List, Dict

def mount_diets_data(file: List) -> List:
    diets = []

    for row in file:
        if len(row) > 0:
            if row[0].isnumeric():
                diet = {
                    'id': int(row[0]),
                    'user_id': row[1],
                    'description': int(row[2])
                }
                diets.append(diet)
    print("Diets data: ", diets)
    return diets
