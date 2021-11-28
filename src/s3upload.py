import os
import boto3
import yaml

# define s3 resource using boto3 
s3_resource = boto3.resource('s3')
s3 = boto3.resource('s3')

# load configs
with open("config/s3_var.yaml", "r") as config:
	try:
		config = yaml.safe_load(config)
		print("\nMy Config = {}\n".format(config))
	except yaml.YAMLError as exc:
		print(exc)

# varaibles
from_local_dir = config['local']['local_dir']
s3_bucket_name = config['upload']['s3_bucket_name']
photo_dir = config['upload']['s3_dir']['photo_dir']
video_dir = config['upload']['s3_dir']['video_dir']
music_dir = config['upload']['s3_dir']['music_dir']
documents_dir = config['upload']['s3_dir']['documents_dir']

# print the content
print("\nMy Local directory = {}\n".format(from_local_dir))
print("\nMy s3 bucket name = {}\n".format(s3_bucket_name))
print("\nMy s3 photo directory = {}\n".format(photo_dir))
print("\nMy s3 video directory = {}\n".format(video_dir))
print("\nMy s3 music directory = {}\n".format(music_dir))
print("\nMy s3 documents directory = {}\n".format(documents_dir))

directory = os.fsencode(from_local_dir)

# main program
def main():
	print("--------->> Inside main method")
	for file in os.listdir(directory):
		filename = os.fsdecode(file)
		if str.upper(filename).endswith(".JPEG") or str.upper(filename).endswith(".JPG") or str.upper(filename).endswith(".PNG") or str.upper(filename).endswith(".HEIC"):
			upload_to_s3(filename, photo_dir, 'image/jpeg')

		if str.upper(filename).endswith(".MOV"):
			upload_to_s3(filename, video_dir, 'video/mov')

		if str.upper(filename).endswith(".MP4"):
			upload_to_s3(filename, video_dir, 'video/mp4')

		if str.upper(filename).endswith(".MP3"):
			upload_to_s3(filename, music_dir, 'audio/mp3')

		else:
			continue


# user defined functions
def upload_to_s3(filename, to_directory, type):
	print("file = {} is moving to s3 dir = {} of type = {}".format(filename, to_directory, type))
	strg = from_local_dir + '/' + filename
	file = open(strg,'rb')
	object = s3.Object(s3_bucket_name, to_directory + filename)
	object.put(Body=file, ContentType = type)


# run main
if __name__ == "__main__":
	main()
