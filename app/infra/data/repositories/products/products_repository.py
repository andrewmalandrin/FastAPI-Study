from typing import List

from app.services.contracts import ProductsRepositoryContract, ProductsData, CreateProductParams
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

    def get_product_by_filters(self, name: str) -> List:
        products = mount_products_data(self.file_manager_instance.read_tsv_file())

        filters = [
            [
                'name', name
            ]
        ]
        try:
            result = self._load_by_filters(filters=filters, data=products)
            print('Returned data:', result)
            return result[0]
        except Exception as error:
            raise ProductNotFound()
