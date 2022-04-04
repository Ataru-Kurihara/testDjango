FROM python:3.9.2-slim
WORKDIR /mysite
ENV PYTHONUNBUFFERED 1
ADD ./mysite/requirements.txt /mysite/
RUN pip install -r requirements.txt