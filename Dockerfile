FROM python:3.9.9-slim-buster
ADD requirements.txt / 
RUN pip3 install -r requirements.txt  -i https://mirrors.aliyun.com/pypi/simple
COPY  . /
CMD [ "sh","script.sh" ]