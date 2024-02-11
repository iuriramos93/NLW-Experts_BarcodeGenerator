from src.views.http_types.http_request import httpRequest
from src.views.http_types.http_response import httpResponse
from src.controllers.tag_creator_controller import CreateTagController
class TagCreatorView:

  def validate_create(self,http_request:httpRequest)->httpResponse:
    body = http_request.body
    product_code = body["product_code"]

    return httpResponse(status_code=200,body={"product_code":product_code})
