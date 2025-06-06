from litestar import Controller, get
from litestar.response import Template
from litestar.status_codes import HTTP_200_OK

from app.config import constants
from litestar.response import Response

from .service import orders_service


class WebController(Controller):
    """Web Controller."""

    include_in_schema = False
    opt = {"exclude_from_auth": True}

    @get(
        path=[constants.SITE_INDEX, f"{constants.SITE_INDEX}/{{path:path}}"],
        operation_id="WebIndex",
        name="frontend:index",
        status_code=HTTP_200_OK,
    )
    async def index(self, path: str | None = None) -> Template:
        """Serve site root."""
        return Template(template_name="site/index.html.j2")

    @get(
        path="/api/orders",
        status_code=HTTP_200_OK,
    )
    async def get_cargo(self) -> Response:
        data = await orders_service.orders(client_name='Efko', params={'state': 'PLAY', 'pure': True})
        return Response(data.json())