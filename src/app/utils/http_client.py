import logging

import httpx


def async_httpx_client(timeout=3, token=None, identity=None, headers=None) -> httpx.AsyncClient:
    client = httpx.AsyncClient(timeout=timeout, verify=False)
    if token:
        client.headers.update({"Authorization": f"Bearer {token}"})
    if identity:
        client.cookies.update({'_identity': identity})
    if headers:
        client.headers.update(headers)
    httpx_logger = logging.getLogger("httpx")
    httpx_logger.setLevel(logging.WARNING)
    return client
