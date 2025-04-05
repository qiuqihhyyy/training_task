from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
import pyshorteners

from database.db import UrlsDAO


router = APIRouter()


# функция по адресу short_url, принимающая в себя short_url и отвечающая полным url
@router.get("/short_url")
async def get_url(short_url):
    # взятие url из базы данных по short_url
    short_url = await UrlsDAO.find_one_or_none_by_url(data_short_url=short_url)
    # добавление полного url в headers
    headers = {"origin_url": f"{short_url.origin_url}", "id": f'{short_url.id}'}
    # отправление ответа на запрос
    return JSONResponse({"message": "short url in header"}, status_code=307, headers=headers)


# функция по адресу shorten-url-id, принимающая в себя id url из базы данных, и отвечающая полным url
@router.get("/short-url-id")
async def get_id(id):
    # взятие url из базы данных по id
    short_url = await UrlsDAO.find_one_or_none_by_id(data_id=id)
    # добавление полного url в headers
    headers = {"origin_url": f"{short_url.origin_url}"}
    # отправление ответа на запрос
    return JSONResponse({"message": "short url in header"}, status_code=307, headers=headers)


# функция по адресу /, принимающая в себя url и дающая в ответ сокращенный url
@router.post('/')
async def post(data=Body()):
    url = data['url']
    # сокращение url через функцию
    short_url = format(shorten_url(url))
    # добавление url в базу данных
    await UrlsDAO.add(short_url=short_url, origin_url=url)
    # отправление ответа на запрос
    return JSONResponse({"short url": short_url, "original_url": url}, status_code=201)


# функция для сокращения url
def shorten_url(url):
    return pyshorteners.Shortener().clckru.short(url)