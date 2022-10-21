from typing import List
from app.domain.usecases.users import DeleteUserContract, DeleteUserParams, DeleteUserResponse
from app.services.contracts import UsersRepositoryContract
from app.services.helpers.http import HttpResponse, HttpStatus
from app.services.errors import UserNotFound

class DeleteUser(DeleteUserContract):
    def __init__(
        self,
        users_repository: UsersRepositoryContract
    ):
        self.users_repository = users_repository
    
    def _mount_response(self, params: List):
        return DeleteUserResponse(
            id=params.get('id', None),
            name=params.get('name', None)
        )

    def execute(self, params: DeleteUserParams) -> HttpResponse[DeleteUserResponse]:
        try:
            deleted_user = self.users_repository.delete_user(id=params.id)
        except UserNotFound:
            return HttpStatus.not_found_404(
                'User not found'
            )

        response = self._mount_response(deleted_user)
        
        return HttpStatus.ok_200(
            response
        )
