from aiohttp import web
from smartnotes import views


app = web.Application()

'''
Routes setup
'''

app.router.add_get('/version', views.version)
app.router.add_post('/annotate', views.version)
