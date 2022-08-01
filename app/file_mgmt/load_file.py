import csv

def tsv_read_file(path):
    print("lendo arquivo: ", path)
    with open(path, 'r', encoding='utf-8') as tsv_file:
        tsv_reader = csv.reader(tsv_file, delimiter='\t')
        line_count = 0
        products = []
        for row in tsv_reader:
            if line_count == 0 or line_count == 1:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                #if row[0] == product_name:
                #lines.append(f'\t Produto: {row[0]}\n\t Porcao: {row[1]}\n\t Carboidratos: {row[2]}\n\t Proteinas: {row[3]}\n\t Gorduras: {row[4]}\n\t Gorduras Saturadas: {row[5]}\n\n')
                product = {
                    'name': row[0],
                    'portion': row[1],
                    'carbohidrates': row[2],
                    'proteins': row[3],
                    'fat': row[4],
                    'saturated_fat': row[5]
                }
                
                products.append(product)
    
    return products

#tsv_read_file('D:/users/pichau/devprojects/training/python/fastapi-study/data/tsf/products.txt', 'Suco de Uva - Del Valle - Macdonalds')