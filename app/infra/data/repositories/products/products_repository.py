from typing import List

from app.services.contracts import ProductsRepositoryContract, ProductsData, CreateProductParams, UpdateProductFileParams, DeleteProductFileParams
from app.infra.data.repositories.helpers import BaseRepository
from app.services.errors import ProductNotFound
from app.services.helpers.products import mount_products_data

class ProductsRepository(BaseRepository, ProductsRepositoryContract):
    def __init__(self, file_manager_instance):
        super().__init__(
            file_manager_instance=file_manager_instance
        )

    def create_product(self, params: CreateProductParams) -> ProductsData:

        product = []

        id = int(self.get_products()[-1]['id']) + 1

        product.append(str(id))
        product.append(params.name)
        product.append(str(params.portion))
        product.append(params.portion_unity)
        product.append(str(params.carbo))
        product.append(str(params.prot))
        product.append(str(params.fat))
        product.append(str(params.saturated_fat))

        line = '\t'.join(product)
        line += '\n'

        self.file_manager_instance.add_line_to_tsv_file(line=line)

        return ProductsData(
            id=id,
            name=params.name,
            portion=params.portion,
            portion_unity=params.portion_unity,
            carbo=params.carbo,
            prot=params.prot,
            fat=params.fat,
            saturated_fat=params.saturated_fat
        )

    def get_products(self) -> List:
        products = mount_products_data(self.file_manager_instance.read_tsv_file())
        return products

    def get_product_by_filters(self, id: int) -> List:
        products = mount_products_data(self.file_manager_instance.read_tsv_file())

        filters = [
            [
                'id', id
            ]
        ]
        try:
            result = self._load_by_filters(filters=filters, data=products)
            print('Returned data:', result)
            return result[0]
        except Exception as error:
            raise ProductNotFound()
        
    def update_product(self, params: UpdateProductFileParams):
        try:
            product_data = self.get_product_by_filters(id=params.id)
        except ProductNotFound:
            raise ProductNotFound()

        file = self.file_manager_instance.read_tsv_file()
        print('File: ', file)

        product = []

        product.append(str(params.id))
        
        items = params.__dict__

        if items['id']:
            del items['id']

        for item in items:
            if items[item] is not None:
                print('Product item changed: ', item)
                product.append(str(items[item]))
            else:
                product.append(str(product_data[item]))

        index = None

        for idx, line in enumerate(file):
            if line[0] == product[0]:
                index=idx

        self.file_manager_instance.update_tsv_file_line(
            file=file,
            new_line=product,
            index=index
        )
        
        print('Product: ', product)

        return {
            'id': int(product[0]),
            'name': product[1],
            'portion': int(product[2]),
            'portion_unity': product[3],
            'carbo': float(product[4]),
            'prot': float(product[5]),
            'fat': float(product[6]),
            'saturated_fat': float(product[7])
        }

    def delete_product(self, params: DeleteProductFileParams):
        try:
            product = self.get_product_by_filters(
                id=int(params.id)
            )
        except Exception as e:
            raise ProductNotFound()
        
        file = self.file_manager_instance.read_tsv_file()
        print('File: ', file)

        index = None

        for idx, line in enumerate(file):
            if line[0] == str(params.id):
                index = idx

        self.file_manager_instance.delete_tsv_file_line(
            file=file,
            index=index
        )

        return {
            'id': product.get('id', None),
            'name': product.get('name', None)
        }
