import config
import json
import os
import glob
import pathlib

from ..service import get_sorted_files_by_date
from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.responses import FileResponse


ROUTER_PREFIX = '/apk'

router = APIRouter(prefix=ROUTER_PREFIX)


@router.get(f'/list')
def get_apk_list():
    '''
    Получаем список apk файлов
    '''
    apk_list = get_sorted_files_by_date(config.APK_FOLDER)
    # apk_list = os.listdir(config.APK_FOLDER)
    return apk_list


@router.get('/download/name/{apk_name}')
def download_apk_by_name(apk_name: str) -> FileResponse:
    '''
    Скачиваем файл по имени
    '''
    if os.path.exists(config.APK_FOLDER.joinpath(apk_name)):
        return FileResponse(str(config.APK_FOLDER.joinpath(apk_name)))
    else:
        raise HTTPException(
            status_code=404,
            detail='APK file not found'
        )
    
@router.get('/download/last')
def download_last_apk() -> FileResponse:
    '''
    Скачиваем послдений обновленный файл
    '''
    apk_list = get_sorted_files_by_date(config.APK_FOLDER)
    apk_name = apk_list
    if len(apk_name) != 0:
        apk_name = apk_name[-1][0]
    else:
        raise HTTPException(
            status_code=404,
            detail='Something went wrong. You may be missing files'
        )
    if os.path.exists(config.APK_FOLDER.joinpath(apk_name)):
        return FileResponse(str(config.APK_FOLDER.joinpath(apk_name)), filename=apk_name)
    else:
        raise HTTPException(
            status_code=404,
            detail='Something went wrong. You may be missing files'
        )
    

@router.post('/upload')
async def upload_apk(file: UploadFile = File(...)):
    if not file.filename.endswith(('.apk')):
        raise HTTPException(status_code=400, detail="Invalid file type. Need apk file")
        
    with open(config.APK_FOLDER.joinpath(file.filename), "wb") as f:
        content = await file.read()
        f.write(content)
    
    return {
        'status': 'OK',
        'filename': file.filename
        }
    