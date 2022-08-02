import csv

# def open_file():
#     PATH = 'D:/users/pichau/devprojects/training/python/fastapi-study/data/tsf/teste.txt'
#     with open(PATH, 'a', encoding='utf-8', newline='') as file:
#         writer_file = csv.writer(file, delimiter='\t')

#     return writer_file

def create_line(product):
    
    newline_array = [product.name, str(product.portion), str(product.carbohidrates), str(product.proteins), str(product.fat), str(product.saturated_fat)]
    newline = '\t'.join(newline_array)
    print(newline)
    write_line(newline_array)

def write_line(line):
    PATH = 'D:/users/pichau/devprojects/training/python/fastapi-study/data/tsf/teste.csv'
    with open(PATH, 'a', encoding='utf-8', newline='') as file:
        writer_file = csv.writer(file, delimiter='\t')
        writer_file.writerow(line)
        file.close()
    pass
