from litestar import Controller, get
from litestar.response import Template
from litestar.status_codes import HTTP_200_OK

from app.config import constants
from litestar.response import Response


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
        data = [
            {
                "id": 803390,
                "status": False,
                "route": {
                    "from": "Воронеж",
                    "fromDesc": "(Воронежская область)",
                    "to": "посёлок Лев Толстой",
                    "toDesc": "Липецкая обл, Лев Толстой п, Пионерская ул, 63",
                },
                "loadingDate": "26.03.2025 06:00",
                "unloadingDate": "26.03.2025 16:00",
                "cargo": {
                    "list": ["ЗМЖ"],
                    "pallet": "24",
                    "weight": "21695",
                },
                "veh": {
                    "type": "Тент",
                    "tonnage": 20,
                },
                "platform": "Алексеевка",
                "cost": "27 766 ₽",
            },
            {
                "id": 803390,
                "status": False,
                "route": {
                    "from": "Воронеж",
                    "fromDesc": "(Воронежская область)",
                    "to": "посёлок Лев Толстой",
                    "toDesc": "Липецкая обл, Лев Толстой п, Пионерская ул, 63",
                },
                "loadingDate": "26.03.2025 06:00",
                "unloadingDate": "26.03.2025 16:00",
                "cargo": {
                    "list": ["ЗМЖ"],
                    "pallet": "24",
                    "weight": "21695",
                },
                "veh": {
                    "type": "Тент",
                    "tonnage": 20,
                },
                "platform": "Алексеевка",
                "cost": "27 766 ₽",
            },
            {
                "id": 803390,
                "status": False,
                "route": {
                    "from": "Воронеж",
                    "fromDesc": "(Воронежская область)",
                    "to": "посёлок Лев Толстой",
                    "toDesc": "Липецкая обл, Лев Толстой п, Пионерская ул, 63",
                },
                "loadingDate": "26.03.2025 06:00",
                "unloadingDate": "26.03.2025 16:00",
                "cargo": {
                    "list": ["ЗМЖ"],
                    "pallet": "24",
                    "weight": "21695",
                },
                "veh": {
                    "type": "Тент",
                    "tonnage": 20,
                },
                "platform": "Алексеевка",
                "cost": "27 766 ₽",
            },
            {
                "id": 803390,
                "status": False,
                "route": {
                    "from": "Воронеж",
                    "fromDesc": "(Воронежская область)",
                    "to": "посёлок Лев Толстой",
                    "toDesc": "Липецкая обл, Лев Толстой п, Пионерская ул, 63",
                },
                "loadingDate": "26.03.2025 06:00",
                "unloadingDate": "26.03.2025 16:00",
                "cargo": {
                    "list": ["ЗМЖ"],
                    "pallet": "24",
                    "weight": "21695",
                },
                "veh": {
                    "type": "Тент",
                    "tonnage": 20,
                },
                "platform": "Алексеевка",
                "cost": "27 766 ₽",
            },
            {
                "id": 803390,
                "status": False,
                "route": {
                    "from": "Воронеж",
                    "fromDesc": "(Воронежская область)",
                    "to": "посёлок Лев Толстой",
                    "toDesc": "Липецкая обл, Лев Толстой п, Пионерская ул, 63",
                },
                "loadingDate": "26.03.2025 06:00",
                "unloadingDate": "26.03.2025 16:00",
                "cargo": {
                    "list": ["ЗМЖ"],
                    "pallet": "24",
                    "weight": "21695",
                },
                "veh": {
                    "type": "Тент",
                    "tonnage": 20,
                },
                "platform": "Алексеевка",
                "cost": "27 766 ₽",
            },
            {
                "id": 803390,
                "status": False,
                "route": {
                    "from": "Воронеж",
                    "fromDesc": "(Воронежская область)",
                    "to": "посёлок Лев Толстой",
                    "toDesc": "Липецкая обл, Лев Толстой п, Пионерская ул, 63",
                },
                "loadingDate": "26.03.2025 06:00",
                "unloadingDate": "26.03.2025 16:00",
                "cargo": {
                    "list": ["ЗМЖ"],
                    "pallet": "24",
                    "weight": "21695",
                },
                "veh": {
                    "type": "Тент",
                    "tonnage": 20,
                },
                "platform": "Алексеевка",
                "cost": "27 766 ₽",
            },
            {
                "id": 803390,
                "status": False,
                "route": {
                    "from": "Воронеж",
                    "fromDesc": "(Воронежская область)",
                    "to": "посёлок Лев Толстой",
                    "toDesc": "Липецкая обл, Лев Толстой п, Пионерская ул, 63",
                },
                "loadingDate": "26.03.2025 06:00",
                "unloadingDate": "26.03.2025 16:00",
                "cargo": {
                    "list": ["ЗМЖ"],
                    "pallet": "24",
                    "weight": "21695",
                },
                "veh": {
                    "type": "Тент",
                    "tonnage": 20,
                },
                "platform": "Алексеевка",
                "cost": "27 766 ₽",
            },
            {
                "id": 803390,
                "status": False,
                "route": {
                    "from": "Воронеж",
                    "fromDesc": "(Воронежская область)",
                    "to": "посёлок Лев Толстой",
                    "toDesc": "Липецкая обл, Лев Толстой п, Пионерская ул, 63",
                },
                "loadingDate": "26.03.2025 06:00",
                "unloadingDate": "26.03.2025 16:00",
                "cargo": {
                    "list": ["ЗМЖ"],
                    "pallet": "24",
                    "weight": "21695",
                },
                "veh": {
                    "type": "Тент",
                    "tonnage": 20,
                },
                "platform": "Алексеевка",
                "cost": "27 766 ₽",
            },
            {
                "id": 803390,
                "status": False,
                "route": {
                    "from": "Воронеж",
                    "fromDesc": "(Воронежская область)",
                    "to": "посёлок Лев Толстой",
                    "toDesc": "Липецкая обл, Лев Толстой п, Пионерская ул, 63",
                },
                "loadingDate": "26.03.2025 06:00",
                "unloadingDate": "26.03.2025 16:00",
                "cargo": {
                    "list": ["ЗМЖ"],
                    "pallet": "24",
                    "weight": "21695",
                },
                "veh": {
                    "type": "Тент",
                    "tonnage": 20,
                },
                "platform": "Алексеевка",
                "cost": "27 766 ₽",
            },
            {
                "id": 803390,
                "status": False,
                "route": {
                    "from": "Воронеж",
                    "fromDesc": "(Воронежская область)",
                    "to": "посёлок Лев Толстой",
                    "toDesc": "Липецкая обл, Лев Толстой п, Пионерская ул, 63",
                },
                "loadingDate": "26.03.2025 06:00",
                "unloadingDate": "26.03.2025 16:00",
                "cargo": {
                    "list": ["ЗМЖ"],
                    "pallet": "24",
                    "weight": "21695",
                },
                "veh": {
                    "type": "Тент",
                    "tonnage": 20,
                },
                "platform": "Алексеевка",
                "cost": "27 766 ₽",
            },
            {
                "id": 803390,
                "status": False,
                "route": {
                    "from": "Воронеж",
                    "fromDesc": "(Воронежская область)",
                    "to": "посёлок Лев Толстой",
                    "toDesc": "Липецкая обл, Лев Толстой п, Пионерская ул, 63",
                },
                "loadingDate": "26.03.2025 06:00",
                "unloadingDate": "26.03.2025 16:00",
                "cargo": {
                    "list": ["ЗМЖ"],
                    "pallet": "24",
                    "weight": "21695",
                },
                "veh": {
                    "type": "Тент",
                    "tonnage": 20,
                },
                "platform": "Алексеевка",
                "cost": "27 766 ₽",
            },
            {
                "id": 803390,
                "status": False,
                "route": {
                    "from": "Воронеж",
                    "fromDesc": "(Воронежская область)",
                    "to": "посёлок Лев Толстой",
                    "toDesc": "Липецкая обл, Лев Толстой п, Пионерская ул, 63",
                },
                "loadingDate": "26.03.2025 06:00",
                "unloadingDate": "26.03.2025 16:00",
                "cargo": {
                    "list": ["ЗМЖ"],
                    "pallet": "24",
                    "weight": "21695",
                },
                "veh": {
                    "type": "Тент",
                    "tonnage": 20,
                },
                "platform": "Алексеевка",
                "cost": "27 766 ₽",
            },
            {
                "id": 803390,
                "status": False,
                "route": {
                    "from": "Воронеж",
                    "fromDesc": "(Воронежская область)",
                    "to": "посёлок Лев Толстой",
                    "toDesc": "Липецкая обл, Лев Толстой п, Пионерская ул, 63",
                },
                "loadingDate": "26.03.2025 06:00",
                "unloadingDate": "26.03.2025 16:00",
                "cargo": {
                    "list": ["ЗМЖ"],
                    "pallet": "24",
                    "weight": "21695",
                },
                "veh": {
                    "type": "Тент",
                    "tonnage": 20,
                },
                "platform": "Алексеевка",
                "cost": "27 766 ₽",
            },
            {
                "id": 803390,
                "status": False,
                "route": {
                    "from": "Воронеж",
                    "fromDesc": "(Воронежская область)",
                    "to": "посёлок Лев Толстой",
                    "toDesc": "Липецкая обл, Лев Толстой п, Пионерская ул, 63",
                },
                "loadingDate": "26.03.2025 06:00",
                "unloadingDate": "26.03.2025 16:00",
                "cargo": {
                    "list": ["ЗМЖ"],
                    "pallet": "24",
                    "weight": "21695",
                },
                "veh": {
                    "type": "Тент",
                    "tonnage": 20,
                },
                "platform": "Алексеевка",
                "cost": "27 766 ₽",
            },
            {
                "id": 803390,
                "status": False,
                "route": {
                    "from": "Воронеж",
                    "fromDesc": "(Воронежская область)",
                    "to": "посёлок Лев Толстой",
                    "toDesc": "Липецкая обл, Лев Толстой п, Пионерская ул, 63",
                },
                "loadingDate": "26.03.2025 06:00",
                "unloadingDate": "26.03.2025 16:00",
                "cargo": {
                    "list": ["ЗМЖ"],
                    "pallet": "24",
                    "weight": "21695",
                },
                "veh": {
                    "type": "Тент",
                    "tonnage": 20,
                },
                "platform": "Алексеевка",
                "cost": "27 766 ₽",
            },
            {
                "id": 803390,
                "status": False,
                "route": {
                    "from": "Воронеж",
                    "fromDesc": "(Воронежская область)",
                    "to": "посёлок Лев Толстой",
                    "toDesc": "Липецкая обл, Лев Толстой п, Пионерская ул, 63",
                },
                "loadingDate": "26.03.2025 06:00",
                "unloadingDate": "26.03.2025 16:00",
                "cargo": {
                    "list": ["ЗМЖ"],
                    "pallet": "24",
                    "weight": "21695",
                },
                "veh": {
                    "type": "Тент",
                    "tonnage": 20,
                },
                "platform": "Алексеевка",
                "cost": "27 766 ₽",
            },
            {
                "id": 803390,
                "status": False,
                "route": {
                    "from": "Воронеж",
                    "fromDesc": "(Воронежская область)",
                    "to": "посёлок Лев Толстой",
                    "toDesc": "Липецкая обл, Лев Толстой п, Пионерская ул, 63",
                },
                "loadingDate": "26.03.2025 06:00",
                "unloadingDate": "26.03.2025 16:00",
                "cargo": {
                    "list": ["ЗМЖ"],
                    "pallet": "24",
                    "weight": "21695",
                },
                "veh": {
                    "type": "Тент",
                    "tonnage": 20,
                },
                "platform": "Алексеевка",
                "cost": "27 766 ₽",
            },
            {
                "id": 803390,
                "status": False,
                "route": {
                    "from": "Воронеж",
                    "fromDesc": "(Воронежская область)",
                    "to": "посёлок Лев Толстой",
                    "toDesc": "Липецкая обл, Лев Толстой п, Пионерская ул, 63",
                },
                "loadingDate": "26.03.2025 06:00",
                "unloadingDate": "26.03.2025 16:00",
                "cargo": {
                    "list": ["ЗМЖ"],
                    "pallet": "24",
                    "weight": "21695",
                },
                "veh": {
                    "type": "Тент",
                    "tonnage": 20,
                },
                "platform": "Алексеевка",
                "cost": "27 766 ₽",
            },
            {
                "id": 803390,
                "status": False,
                "route": {
                    "from": "Воронеж",
                    "fromDesc": "(Воронежская область)",
                    "to": "посёлок Лев Толстой",
                    "toDesc": "Липецкая обл, Лев Толстой п, Пионерская ул, 63",
                },
                "loadingDate": "26.03.2025 06:00",
                "unloadingDate": "26.03.2025 16:00",
                "cargo": {
                    "list": ["ЗМЖ"],
                    "pallet": "24",
                    "weight": "21695",
                },
                "veh": {
                    "type": "Тент",
                    "tonnage": 20,
                },
                "platform": "Алексеевка",
                "cost": "27 766 ₽",
            },
            {
                "id": 803390,
                "status": False,
                "route": {
                    "from": "Воронеж",
                    "fromDesc": "(Воронежская область)",
                    "to": "посёлок Лев Толстой",
                    "toDesc": "Липецкая обл, Лев Толстой п, Пионерская ул, 63",
                },
                "loadingDate": "26.03.2025 06:00",
                "unloadingDate": "26.03.2025 16:00",
                "cargo": {
                    "list": ["ЗМЖ"],
                    "pallet": "24",
                    "weight": "21695",
                },
                "veh": {
                    "type": "Тент",
                    "tonnage": 20,
                },
                "platform": "Алексеевка",
                "cost": "27 766 ₽",
            },
            {
                "id": 803390,
                "status": False,
                "route": {
                    "from": "Воронеж",
                    "fromDesc": "(Воронежская область)",
                    "to": "посёлок Лев Толстой",
                    "toDesc": "Липецкая обл, Лев Толстой п, Пионерская ул, 63",
                },
                "loadingDate": "26.03.2025 06:00",
                "unloadingDate": "26.03.2025 16:00",
                "cargo": {
                    "list": ["ЗМЖ"],
                    "pallet": "24",
                    "weight": "21695",
                },
                "veh": {
                    "type": "Тент",
                    "tonnage": 20,
                },
                "platform": "Алексеевка",
                "cost": "27 766 ₽",
            },
            {
                "id": 803390,
                "status": False,
                "route": {
                    "from": "Воронеж",
                    "fromDesc": "(Воронежская область)",
                    "to": "посёлок Лев Толстой",
                    "toDesc": "Липецкая обл, Лев Толстой п, Пионерская ул, 63",
                },
                "loadingDate": "26.03.2025 06:00",
                "unloadingDate": "26.03.2025 16:00",
                "cargo": {
                    "list": ["ЗМЖ"],
                    "pallet": "24",
                    "weight": "21695",
                },
                "veh": {
                    "type": "Тент",
                    "tonnage": 20,
                },
                "platform": "Алексеевка",
                "cost": "27 766 ₽",
            },
            {
                "id": 803390,
                "status": False,
                "route": {
                    "from": "Воронеж",
                    "fromDesc": "(Воронежская область)",
                    "to": "посёлок Лев Толстой",
                    "toDesc": "Липецкая обл, Лев Толстой п, Пионерская ул, 63",
                },
                "loadingDate": "26.03.2025 06:00",
                "unloadingDate": "26.03.2025 16:00",
                "cargo": {
                    "list": ["ЗМЖ"],
                    "pallet": "24",
                    "weight": "21695",
                },
                "veh": {
                    "type": "Тент",
                    "tonnage": 20,
                },
                "platform": "Алексеевка",
                "cost": "27 766 ₽",
            },
            {
                "id": 803390,
                "status": False,
                "route": {
                    "from": "Воронеж",
                    "fromDesc": "(Воронежская область)",
                    "to": "посёлок Лев Толстой",
                    "toDesc": "Липецкая обл, Лев Толстой п, Пионерская ул, 63",
                },
                "loadingDate": "26.03.2025 06:00",
                "unloadingDate": "26.03.2025 16:00",
                "cargo": {
                    "list": ["ЗМЖ"],
                    "pallet": "24",
                    "weight": "21695",
                },
                "veh": {
                    "type": "Тент",
                    "tonnage": 20,
                },
                "platform": "Алексеевка",
                "cost": "27 766 ₽",
            },
            {
                "id": 803390,
                "status": False,
                "route": {
                    "from": "Воронеж",
                    "fromDesc": "(Воронежская область)",
                    "to": "посёлок Лев Толстой",
                    "toDesc": "Липецкая обл, Лев Толстой п, Пионерская ул, 63",
                },
                "loadingDate": "26.03.2025 06:00",
                "unloadingDate": "26.03.2025 16:00",
                "cargo": {
                    "list": ["ЗМЖ"],
                    "pallet": "24",
                    "weight": "21695",
                },
                "veh": {
                    "type": "Тент",
                    "tonnage": 20,
                },
                "platform": "Алексеевка",
                "cost": "27 766 ₽",
            }
        ]
        return Response(data)