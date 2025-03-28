from fastapi import FastAPI, Body, Response
from fastapi.responses import JSONResponse
import pyshorteners

from db import UrlsDAO

app = FastAPI()


@app.get("/short_url")
async def get_url(short_url):
    short_url = await UrlsDAO.find_one_or_none_by_url(data_short_url=short_url)
    headers = {"short_url": f"{short_url.origin_url}", "id": f'{short_url.id}'}
    return JSONResponse({"message": "short url in header"}, status_code=307, headers=headers)


@app.get("/shorten-url-id")
async def get_id(id):
    short_url = await UrlsDAO.find_one_or_none_by_id(data_id=id)
    headers = {"short_url": f"{short_url.origin_url}"}
    return JSONResponse({"message": "short url in header"}, status_code=307, headers=headers)


@app.post('/')
async def post(data=Body()):
    url = data['url']
    short_url = format(shorten_url(url))
    await UrlsDAO.add(short_url=short_url, origin_url=url)
    return JSONResponse({"short url": short_url, "original_url":url}, status_code=201)


def shorten_url(url):
    return pyshorteners.Shortener().clckru.short(url)



