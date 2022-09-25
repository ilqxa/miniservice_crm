import os
import sys
import aiohttp
import logging
from aiohttp import web
from typing import Optional

from .objects import *

DOMAIN = os.environ.get('DOMAIN', '')
TG_API_URL = os.environ.get('TG_API_URL', '')
TG_API_KEY = os.environ.get("TG_API_KEY", '')
TG_ENTRYPOINT = os.environ.get("TG_ENTRYPOINT", '')

class Handler:
    def __init__(self) -> None:
        self.setWebhook()
        self.session = aiohttp.ClientSession(TG_API_URL)

    def __del__(self) -> None:
        self.session.close()
        del self.session

    async def receive(self, request: web.Request) -> web.Response:
        logging.info('Request was received')
        data = await request.json()

    async def get_request(self, point:str, params:dict={}) -> web.Response:
        headers = {'Content-Type': 'application/json'}
        async with self.session.get(f'{TG_API_KEY}/{point}', json=params, headers=headers) as resp:
            logging.info(f'Get-request was made with the status: {resp.status}')
            return resp
    
    async def post_request(self, point:str, json:dict={}) -> web.Response:
        headers = {'Content-Type': 'application/json'}
        async with self.session.post(f'{TG_API_KEY}/{point}', json=json, headers=headers) as resp:
            logging.info(f'Post-request was made with the status: {resp.status}')
            return resp

    async def reaction(self, upd:Update) -> None:
        if upd.message is not None and upd.message.chat is not None:
            await self.sendMessage(
                chat_id = upd.message.chat.id,
                test = upd.message.text,
            )

    async def setWebhook(self) -> None:
        params = {
            'url': f'{DOMAIN}/{TG_ENTRYPOINT}',
        }
        logging.info(f'Trying to set webhook with the params {params}')
        resp = await self.get_request('setWebhook', params=params)
        if resp.json()['ok']:
            logging.info(f'Entry: {DOMAIN}/{TG_ENTRYPOINT}')
            logging.info(resp.text)
        else:
            logging.error(resp.json())
            sys.exit('Unable to establish a connection to telegram')

    async def sendMessage(
        self,
        chat_id:int,
        text:str,
    ) -> None:
        message = {
            'chat_id': chat_id,
            'text': text,
        }
        _ = await self.post_request('sendMessage', json=message)