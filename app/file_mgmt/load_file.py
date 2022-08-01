import csv

def get_product_by_name(product_name):
    products = tsv_read_file()
    for product in products:
        if product['name'].capitalize() == product_name.capitalize():
            print(product['name'])
            return product
    raise Exception("Error: no product matches the name passed in the path")

def calculate_by_portion(product, portion):
        
    product['carbohidrates'] = round((product['carbohidrates'] /  product['portion']) * portion, 2)
    product['proteins'] = round((product['proteins'] /  product['portion']) * portion, 2)
    product['fat'] = round((product['fat'] /  product['portion']) * portion, 2)
    product['saturated_fat'] = round((product['saturated_fat'] /  product['portion']) * portion, 2)
    product['portion'] = portion

    return product

def tsv_read_file():
    path = 'D:/users/pichau/devprojects/training/python/fastapi-study/data/tsf/products.txt'
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
                    'portion': int(row[1]),
                    'carbohidrates': float(row[2]),
                    'proteins': float(row[3]),
                    'fat': float(row[4]),
                    'saturated_fat': float(row[5])
                }
                
                products.append(product)
    
    return products



#tsv_read_file('D:/users/pichau/devprojects/training/python/fastapi-study/data/tsf/products.txt', 'Suco de Uva - Del Valle - Macdonalds')