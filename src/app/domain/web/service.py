from abc import ABC, abstractmethod
from typing import Coroutine, Any

from app.utils.decorators import exceptions_wrapped
from app.utils.http_client import async_httpx_client
from httpx import HTTPStatusError, AsyncClient, Response


class Abstract(ABC):
    http_client: ...

    @abstractmethod
    def orders(self, client_name: str, params: Any) -> ...:
        ...

    @abstractmethod
    def order(self, client_name: str, fltr: Any) -> ...:
        ...

    @abstractmethod
    def shutdown(self) -> ...:
        ...


class Base(Abstract):
    http_client: AsyncClient = async_httpx_client()

    def orders(self, client_name: str, params: dict) -> Coroutine[Any, Any, Response]:
        return self.http_client.get(url=f"https://orders.ru.tuna.am/biddings/{client_name}/orders", params=params)

    def order(self, client_name: str, fltr: dict) -> Coroutine[Any, Any, Response]:
        return self.http_client.post(url=f"https://orders.ru.tuna.am/biddings/{client_name}/order", json=fltr)

    def shutdown(self) -> Coroutine[Any, Any, None]:
        return self.http_client.aclose()


class OrdersService(Base): ...


orders_service = OrdersService()
