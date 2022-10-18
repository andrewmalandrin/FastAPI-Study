from app.domain.usecases import GetProductContract, GetProductParams, GetProductResponse
from app.services.contracts import ProductsRepositoryContract
from app.services.helpers.http import HttpResponse
from app.services.helpers.http.http import HttpStatus
from app.services.errors import ProductNotFound
from typing import List


class GetProduct(GetProductContract):
    def __init__(
        self,
        products_repository: ProductsRepositoryContract
    ) -> None:
        self.products_repository = products_repository
    
    def _calculate_portion(self, portion: int, product: List):
        
        calculated_product = {}

        calculated_product['id'] = product['id']
        calculated_product['name'] = product['name']
        calculated_product['portion'] = portion
        calculated_product['portion_unity'] = product['portion_unity']
        calculated_product['carbohidrates'] = round((product['carbohidrates']/product['portion']) * portion, 2)
        calculated_product['proteins'] = round((product['proteins']/product['portion']) * portion, 2)
        calculated_product['fat'] = round((product['fat']/product['portion']) * portion, 2)
        calculated_product['saturated_fat'] = round((product['saturated_fat']/product['portion']) * portion, 2)

        return calculated_product
    
    def execute(self, params: GetProductParams) -> HttpResponse[GetProductResponse]:
        try:
            product = self.products_repository.get_product_by_filters(id=params.id)
        except ProductNotFound:
            return HttpStatus.not_found_404('Product not found')

        if params.portion:
            product = self._calculate_portion(params.portion, product)

        
        return HttpStatus.ok_200(
            GetProductResponse(
                id=product['id'],
                name=product['name'],
                portion=product['portion'],
                portion_unity=product['portion_unity'],
                carbo=product['carbohidrates'],
                prot=product['proteins'],
                fat=product['fat'],
                saturated_fat=product['saturated_fat']
            )
        )
