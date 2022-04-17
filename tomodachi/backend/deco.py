from __future__ import annotations

from typing import (
    Callable,
    Coroutine,
    TYPE_CHECKING,
    Any
)

if TYPE_CHECKING:
    from starlette.requests import Request
    from starlette.responses import Response

    RouteT = Callable[[Request], Coroutine[Any, Any, Response]]


def route(path: str):
    def decorator(func: RouteT):
        func.__is_route__ = True
        func.__route_path__ = path
        return func

    return decorator