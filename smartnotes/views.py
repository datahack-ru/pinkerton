from aiohttp import web

from smartnotes.settings import PROJECT_VERSION


async def version(request):
    return web.json_response(data={
        'version': PROJECT_VERSION,
    })
