import os
import sys
import logging
import requests
import aiohttp
from aiohttp import web

logging.basicConfig(level=logging.INFO)

# Server params
DOMAIN = os.environ.get('DOMAIN', '')
PORT = int(os.environ.get('PORT', 10000))

# Telegram params
TG_API_URL = os.environ.get('TG_API_URL', '')
TG_API_KEY = os.environ.get("TG_API_KEY", '')

# SSL params
SERT_PEM = os.environ.get("SERT_PEM", '')

# Entrypoints
TG_ENTRYPOINT = os.environ.get("TG_ENTRYPOINT", '')
IN_ENTRYPOINT = os.environ.get("IN_ENTRYPOINT", '')
logging.info('Env variables were obtained')

def set_webhook()->None:
    url = f'{TG_API_URL}/{TG_API_KEY}/setWebhook'
    params = {'url': f'{DOMAIN}/{TG_ENTRYPOINT}'}
    files = None#{'certificate': ('@sert.pem', SERT_PEM)}
    res = requests.get(url, params=params, files=files)
    if res.json()['ok']:
        logging.info(f'Entry: {DOMAIN}/{TG_ENTRYPOINT}')
        logging.info(res.text)
    else:
        logging.error(res.json())
        sys.exit('Unable to establish a connection to telegram')

if __name__ == '__main__':
    # set_webhook()
    app = web.Application()
    app.add_routes([
        web.get(f'/pulse', web.Response(status=200)),
        # web.post(f'/{TG_ENTRYPOINT}', web.Response(status=200)),
        # web.get(f'/{IN_ENTRYPOINT}', web.Response(status=200)),
    ])
    web.run_app(app, host='0.0.0.0', port=PORT)