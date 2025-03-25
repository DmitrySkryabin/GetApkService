import config
import os

from fastapi import FastAPI
from app.routers import apk_router

if config.ROOT_PATH is not None:
    app = FastAPI(
        root_path=f'/{config.ROOT_PATH}',
        docs_url='/docs',
        openapi_url='/openapi.json'
        )
else:
    app = FastAPI()

app.include_router(apk_router.router)

'''
Создаем папку где будем хранить Apk, если ее не существует
'''
if not os.path.exists(config.APK_FOLDER):
    os.makedirs(config.APK_FOLDER)
    print(f"Directory '{config.APK_FOLDER}' created.")
else:
    print(f"Directory '{config.APK_FOLDER}' already exists.")

@app.get("/")
def main():
    return {
        'name': 'GetApkService',
        'version': config.VERISION,
        'help': 'TO USE: \n to load apk go to "/apk/download/last'
    }