import os
import sys
import logging
import requests
import aiohttp
from aiohttp import web

from telegram import bot

logging.basicConfig(level=logging.INFO)

# Server params
PORT = int(os.environ.get('PORT', 10000))
TG_ENTRYPOINT = os.environ.get("TG_ENTRYPOINT", '')

async def pulse(req: web.Request) -> web.Response:
    return web.Response(status=200)

if __name__ == '__main__':
    app = web.Application()
    tg_bot = bot.Handler()
    app.add_routes([
        web.get(f'/pulse', pulse),
        web.post(f'/{TG_ENTRYPOINT}', tg_bot.receive),
    ])
    web.run_app(app, host='0.0.0.0', port=PORT)