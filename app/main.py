import config

from fastapi import FastAPI
from app.routers import apk_router

app = FastAPI()

app.include_router(apk_router.router)

@app.get("/")
def main():
    return {
        'name': 'GetApkService',
        'version': config.VERISION,
        'help': 'TO USE: \n to load apk go to "/apk/download/last'
    }