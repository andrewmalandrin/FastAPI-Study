from app.services.contracts import UsersData
from typing import List

def mount_users_data(file: List) -> UsersData:
    users = []

    for row in file:
        if row[0].isnumeric():
            user = {
                'id': int(row[0]),
                'name': row[1],
                'weight': float(row[2]),
                'carbo_kg': float(row[3]),
                'fat_kg': float(row[4]),
                'age': float(row[5])
            }
            users.append(user)

    return users
