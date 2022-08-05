import csv
from app.models.basemodel.responses import BasicResponseBase

# def open_file():
#     PATH = 'D:/users/pichau/devprojects/training/python/fastapi-study/data/tsf/teste.txt'
#     with open(PATH, 'a', encoding='utf-8', newline='') as file:
#         writer_file = csv.writer(file, delimiter='\t')

#     return writer_file

def create_line(product):
    try:
        newline_array = [product.name, str(product.portion), str(product.carbohidrates), str(product.proteins), str(product.fat), str(product.saturated_fat)]
        newline = '\t'.join(newline_array)
        print(newline)
        write_line(newline_array)
        response = BasicResponseBase(status_code=200, message='Produto adicionado com sucesso')
    except Exception as exception:
        response = BasicResponseBase(status_code=400, message='Houve um erro na adição do produto')

    return response


def write_line(line):
    PATH = 'D:/users/pichau/devprojects/training/python/fastapi-study/data/tsf/teste.csv'
    with open(PATH, 'a', encoding='utf-8', newline='') as file:
        writer_file = csv.writer(file, delimiter='\t')
        writer_file.writerow(line)
        file.close()
    pass
