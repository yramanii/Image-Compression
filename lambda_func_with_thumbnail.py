import json
import boto3
import uuid
import PIL
import urllib.parse
from PIL import Image
import os
import sys


sys.path.insert(1, '/tmp/')


s3_client = boto3.client('s3')




def compress_me(key, download_path, resized_path, upload_path_thumbnail):
    """
    Compress the images.
    Input: str -> download_path, str -> resized_path
    Output: int -> compression percentage
    """
    
    
    try:
        picture = Image.open(download_path)
        print(key)
        
        Thumbnail_Dimensions = (400, 450)
        Picture_Dimensions = (1000, 1000)
        if picture.size > (1200,1200):
            new_size = picture.resize(Picture_Dimensions)
            
            if ".png" in key.lower():
                compressed = new_size.convert("P", palette=Image.ADAPTIVE, colors=256)
                compressed.save(resized_path, "PNG", optimize=True, quality=85)
                
                picture.thumbnail(Thumbnail_Dimensions)
                picture.save(upload_path_thumbnail, "PNG",optimize=True,quality=85)
            else:
                new_size.save(resized_path, "JPEG", optimize=True, quality=85)
                
                picture.thumbnail(Thumbnail_Dimensions)
                picture.save(upload_path_thumbnail, "JPEG",optimize=True,quality=85)
            return "success"
            
        else:
            if ".png" in key.lower():
                compressed = picture.convert("P", palette=Image.ADAPTIVE, colors=256)
                compressed.save(resized_path, "PNG", optimize=True, quality=85)
                
                picture.thumbnail(Thumbnail_Dimensions)
                picture.save(upload_path_thumbnail, "PNG",optimize=True,quality=85)
            else:
                picture.save(resized_path, "JPEG", optimize=True, quality=85)
                
                picture.thumbnail(Thumbnail_Dimensions)
                picture.save(upload_path_thumbnail, "JPEG",optimize=True,quality=85)
            return "success"
        
        
    except Exception as e:
        return f"compression failed with error: {str(e)}"
        
        
def lambda_handler(event, context):
    
    
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    # print(bucket)
    key = urllib.parse.unquote_plus(
        event["Records"][0]["s3"]["object"]["key"], encoding="utf-8"
    )
    print(key)
    folder_struc = '/'.join(key.split('/')[:-1])
    # print(folder_struc)
    tmpkey = key.split('/')[-1]
    # print(tmpkey)
    download_path = "/tmp/{}{}".format(uuid.uuid4(), tmpkey)
    upload_path = "/tmp/resized-{}".format(tmpkey)
    upload_path_thumbnail = "/tmp/thumbnail-{}".format(tmpkey)
    print(upload_path)
    s3_client.download_file(bucket, key, download_path)
    
    
    if key.lower().split('.')[-1] in ("jpg", "jpeg", "png"):
        result = compress_me(key, download_path, upload_path, upload_path_thumbnail)
        s3_client.upload_file(upload_path, 'compressed-imgs-beautytap-django-dev', key)
        s3_client.upload_file(upload_path_thumbnail, 'compressed-imgs-beautytap-django-dev', folder_struc+'/'+"thumbnail_"+tmpkey)
    else:
        result = "File extension not proper."
        
        
    return {"statusCode": 200, "body": json.dumps(result)}
    