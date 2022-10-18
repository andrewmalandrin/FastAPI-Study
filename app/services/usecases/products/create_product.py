from app.domain.usecases import CreateProductContract, CreateProductParams, CreateProductResponse

from app.services.contracts import ProductsRepositoryContract
from app.services.helpers.http import HttpResponse
from app.services.helpers.http.http import HttpStatus

class CreateProduct(CreateProductContract):
    def __init__(
        self,
        products_repository: ProductsRepositoryContract
    ):
        self.products_repository = products_repository
    def execute(self, params: CreateProductParams) -> HttpResponse[CreateProductResponse]:

        product = self.products_repository.create_product(params)
        
        return HttpStatus.created_201(
            CreateProductResponse(
                id=product.id,
                name=product.name,
                portion=product.portion,
                portion_unity=product.portion_unity,
                carbo=product.carbo,
                prot=product.prot,
                fat=product.fat,
                saturated_fat=product.saturated_fat
            )
        )
