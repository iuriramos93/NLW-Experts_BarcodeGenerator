from src.views.http_types.http_response import httpResponse
from .errors_types.http_unprocessable_entity import HttpUnprocessableEntityError

def handler_error(error:Exception)-> httpResponse:
  if isinstance(error,HttpUnprocessableEntityError):
    return httpResponse(
      status_code=error.status_code,
      body={
        "error":[{
          "title": error.name,
          "datail":error.message
        }]
        }
      )

  return httpResponse(status_code=500,
                      body= {"error":[{
                        "title":"Server Error",
                        "datail":str(error)

                       }
                    ]
                  }
                )