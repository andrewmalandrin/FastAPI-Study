from traceback import format_exc
from typing import Any

from app.domain.usecases import Usecase
from app.services.helpers.http import HttpResponse, HttpRequest, HttpStatus
from app.services.helpers.http.http import HttpError

def fastapi_adapter(request: Any, usecase: Usecase) -> HttpResponse:
    try:
        http_request = HttpRequest(
            header=request['headers'],
            body=request['body'],
            query=request['query']
        )
        response = usecase.execute(http_request.body)

    except HttpError as error:
        print(f'Erro, {error.message} - {error.status_code}')
        return HttpResponse(status_code=error.status_code, body={'error': error.message})

    except Exception:
        print(f'Erro desconhecido na execução do caso de uso{format_exc()}')
        return HttpStatus.internal_server_error_500

    return response
