import csv

def open_file():
    PATH = 'D:/users/pichau/devprojects/training/python/fastapi-study/data/tsf/teste.txt'
    with open(PATH, 'w', encoding='utf-8', newline='') as file:
        writer_file = csv.writer(file, delimiter='\t')

    return writer_file

def create_line(product):

    return

def add_line(writer_file, product):
    
    writer_file.writerow(product['name'], product['portion'], product['carbohidrates'], product['proteins'], product['fat'], product['saturated_fat'])

                    # 'name': row[0],
                    # 'portion': int(row[1]),
                    # 'carbohidrates': float(row[2]),
                    # 'proteins': float(row[3]),
                    # 'fat': float(row[4]),
                    # 'saturated_fat': float(row[5])