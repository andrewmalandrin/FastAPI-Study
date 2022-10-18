from app.domain.usecases import UpdateProductContract, UpdateProductParams, UpdateProductResponse
from app.services.contracts import ProductsRepositoryContract
from app.services.helpers.http import HttpResponse
from app.services.helpers.http.http import HttpStatus
from app.services.errors import ProductNotFound



class UpdateProduct(UpdateProductContract):
    def __init__(
        self,
        products_repository: ProductsRepositoryContract
    ) -> None:
        self.products_repository = products_repository
    
    def execute(self, params: UpdateProductParams) -> HttpResponse[UpdateProductResponse]:
        try:
            product = self.products_repository.update_product(
                UpdateProductParams(
                    id=params.id,
                    name=params.name,
                    portion=params.portion,
                    portion_unity=params.portion_unity,
                    carbo=params.carbo,
                    prot=params.prot,
                    fat=params.fat,
                    saturated_fat=params.saturated_fat
                )
            )
        except ProductNotFound:
            return HttpStatus.not_found_404('Product not found')
        
        return HttpStatus.accepted_202(
            UpdateProductResponse(
                id=product['id'],
                name=product['name'],
                portion=product['portion'],
                portion_unity=product['portion_unity'],
                carbo=product['carbo'],
                prot=product['prot'],
                fat=product['fat'],
                saturated_fat=product['saturated_fat']
            )
        )
