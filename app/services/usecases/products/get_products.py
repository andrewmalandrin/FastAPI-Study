from typing import List

from app.infra.data.repositories.products import products_repository
from app.services.contracts import ProductsRepositoryContract
from app.domain.usecases import GetProductsContract, GetProductsResponse, Product
from app.services.helpers.http import HttpResponse
from app.services.helpers.http.http import HttpStatus


class GetProducts(GetProductsContract):
    def __init__(
        self,
        products_repository: ProductsRepositoryContract
    ) -> None:
        self.products_repository = products_repository

    def _mount_response(self, products: List[Product]) -> GetProductsResponse:
        
        products_list = []
        for product in products:
            products_list.append(
                Product(
                    name=product['name'],
                    portion=product['portion'],
                    portion_unity=product['portion_unity'],
                    carbo=product['carbohidrates'],
                    prot=product['proteins'],
                    fat=product['fat'],
                    saturated_fat=product['saturated_fat']
                )
            )
        return GetProductsResponse(
            products=products_list
        )
        
    def execute(self, params) -> HttpResponse[GetProductsResponse]:
        
        products=self.products_repository.get_products()
        response = self._mount_response(products)
        
        return HttpStatus.ok_200(
            response
            # GetProductsResponse(
            #     products=self.products_repository.get_products()
            # )
        )