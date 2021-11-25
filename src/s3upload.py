import boto3
import os


s3_resource = boto3.resource(
    's3',
     aws_access_key_id='', 
     aws_secret_access_key='', 
)


s3 = boto3.resource('s3')

directory_in_str="photos"

directory = os.fsencode(directory_in_str)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if str.upper(filename).endswith(".JPEG") or str.upper(filename).endswith(".JPG") or str.upper(filename).endswith(".PNG") or str.upper(filename).endswith(".HEIC"):
        strg=directory_in_str+'/'+filename
        print(strg)     
        file = open(strg,'rb')
        object = s3.Object('factspan-mac-backup','Photos/2021/November/'+filename)
        object.put(Body=file,ContentType='image/jpeg')

    if str.upper(filename).endswith(".MOV"):
        strg=directory_in_str+'/'+filename
        print(strg)     
        file = open(strg,'rb')
        object = s3.Object('factspan-mac-backup','Videos/2021/November/'+filename)
        object.put(Body=file,ContentType='video/mov')

    if str.upper(filename).endswith(".MP4"):
        strg=directory_in_str+'/'+filename
        print(strg)     
        file = open(strg,'rb')
        object = s3.Object('factspan-mac-backup','Videos/2021/November/'+filename)
        object.put(Body=file,ContentType='video/mp4')

    if str.upper(filename).endswith(".MP3"):
        strg=directory_in_str+'/'+filename
        print(strg)     
        file = open(strg,'rb')
        object = s3.Object('factspan-mac-backup','Music/2021/November/'+filename)
        object.put(Body=file,ContentType='audio/mp3')

    else:
        continue
