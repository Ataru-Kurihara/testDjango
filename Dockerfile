FROM python:3.9.2-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /mysite
ADD ./mysite/requirements.txt /mysite/
RUN pip install -r requirements.txt