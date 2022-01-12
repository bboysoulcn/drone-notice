FROM python:3.11.0a3-alpine3.15
ADD requirements.txt / 
RUN pip3 install -r requirements.txt  -i https://mirrors.aliyun.com/pypi/simple
COPY  . /
CMD [ "python3", "/main.py" ]