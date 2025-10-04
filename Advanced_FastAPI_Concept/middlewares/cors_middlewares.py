from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # Define which sites can call your API
    allow_origins=[
        'https://my-frontend.com',    #only this website can call the API
        'http://localhost:3000'     # for local testing
]
    ,
    allow_credentials=True,  #allow cookies/auth
    allow_methods=['GET', 'POST', 'PUT', 'DELETE'],  #allow only these methods
    allow_headers=['*']   # allow all headers
)
#define your endpoint 