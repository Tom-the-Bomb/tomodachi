from __future__ import annotations

from typing import TYPE_CHECKING

from deco import route

if TYPE_CHECKING:
    from starlette.requests import Request

@route('/')
async def index(request: Request):
    app = request.app
    ctx = {'request': request}
    return app.tpl.TemplateResponse('index.html', ctx)