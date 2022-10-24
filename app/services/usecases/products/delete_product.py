from app.domain.usecases import DeleteProductContract, DeleteProductParams, DeleteProductResponse
from app.services.contracts import ProductsRepositoryContract, DeleteProductFileParams
from app.services.helpers.http import HttpResponse
from app.services.helpers.http.http import HttpStatus
from app.services.errors import ProductNotFound

class DeleteProduct(DeleteProductContract):
    def __init__(
        self,
        products_repository=ProductsRepositoryContract
    ):
        self.products_repository = products_repository

    def execute(self, params: DeleteProductParams) -> HttpResponse[DeleteProductResponse]:
        try:
            product = self.products_repository.delete_product(
                params=DeleteProductFileParams(
                    id=params.id
                )
            )
        except ProductNotFound:
            return HttpStatus.not_found_404(
                'Product not found'
            )

        return HttpStatus.accepted_202(
            DeleteProductResponse(
                id=product.get('id', None),
                name=product.get('name', None),
            )
        )
