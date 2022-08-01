import csv
import unidecode

def tsv_read_file(path, product_name):
    print("lendo arquivo: ", path)
    with open(path) as tsv_file:
        tsv_reader = csv.reader(tsv_file, delimiter='\t')
        line_count = 0
        for row in tsv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                if row[0] == product_name:
                    print(f'\t Produto: {row[0]}\n\t Porcao: {row[1]}\n\t Carboidratos: {row[2]}\n\t Proteinas: {row[3]}\n\t Gorduras: {row[4]}\n\t Gorduras Saturadas: {row[5]}\n\n')

    
    return tsv_reader

tsv_read_file('D:/users/pichau/devprojects/training/python/fastapi-study/data/tsf/products.txt', 'Suco de Uva - Del Valle - Macdonalds')