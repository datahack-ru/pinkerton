from aiohttp import web

from pinkerton.app import app
from pinkerton.settings import BIND_HOST, BIND_PORT


web.run_app(app, host=BIND_HOST, port=BIND_PORT)
