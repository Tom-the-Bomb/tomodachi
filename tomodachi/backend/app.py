import os
from inspect import getmembers
from importlib import import_module

from starlette.applications import Starlette
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from starlette.routing import Mount, Route


class TomodachiApp(Starlette):
    tpl = Jinja2Templates('../frontend/tps/')

routes: list[Mount] = [
    Mount('/static', app=StaticFiles(directory='../frontend/static/')) # load static files
]

# Load routes
for filename in os.listdir('../backend/routes'):
    if not filename.endswith('.py'):
        continue

    module = import_module(f'routes.{filename[:-3]}')

    for _, value in getmembers(module):
        if getattr(value, '__is_route__', None):
            print('is route')
            routes.append(Route(value.__route_path__, value)) # type: ignore

                
app = TomodachiApp(routes=routes)
