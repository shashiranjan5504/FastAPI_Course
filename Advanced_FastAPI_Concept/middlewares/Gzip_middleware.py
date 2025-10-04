from fastapi import FastAPI
from starlette.middleware.gzip import GZipMiddleware

app=FastAPI()

app.add_middleware(
    GZipMiddleware,minimum_size=1000  #it tells the response is compressed only if its size is gt minimum size
)