from aiohttp import web

from smartnotes.app import app
from smartnotes.settings import BIND_HOST, BIND_PORT


web.run_app(app, host=BIND_HOST, port=BIND_PORT)
