from PIL import Image
from config import BaseConfig
from datetime import datetime
import os
import requests
import logging


def download(URL, name):

    resp = requests.get(URL, stream=True)

    if not resp.ok:
        print('DOWNLOAD ERROR')
    
    with open('{}', 'wb') as img:
    for block in resp.iter_content(1024):
        if not block:
            break
            # logging status, URL, time
        img.write(block)

        
def insert_logo(image_name):
    now = datetime.now()
    logo_path = BaseConfig.LOGO_PATH
    logo_name = '{}/logo.png'.format('logo.png')
    logo = Image.open(logo_name)
    box = BaseConfig.BOX
    image_directory = BaseConfig.IMAGE_DIRECTORY
    file_name = '{}/image_{}'.format(image_directory, 
                                     now.strftime('%Y-%m-%dT%H:%M:%S'))

    try:
        img = Image.open(image_name)
        img.paste(logo, box, mask=logo)
        img.save(file_name, format='png')
    except IOError:
        # log image, url, datetime

    


