FROM python:3.9.9-slim-buster
WORKDIR /app
ADD requirements.txt /app 
RUN pip3 install -r requirements.txt  -i https://mirrors.aliyun.com/pypi/simple
ADD . /app
CMD [ "sh","script.sh" ]