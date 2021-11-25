# set base image (host OS)
FROM python:3.8

LABEL maintainer="Sebastian Srikanth Kumar <sebastin.kumar@factspan.com>"


RUN apt-get update && apt-get clean 

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

RUN pip install --upgrade awscli

ARG AWS_KEY=''
ARG AWS_SECRET_KEY=''
ARG AWS_REGION=''

RUN aws configure set aws_access_key_id $AWS_KEY \
&& aws configure set aws_secret_access_key $AWS_SECRET_KEY \
&& aws configure set default.region $AWS_REGION
