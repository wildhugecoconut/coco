FROM python:3.10-slim-bullseye
LABEL project = "nuclio-ml-flask-api"
LABEL version="1.0"
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt \
	&& python3 train.py
CMD ["python3","-u","app.py"]


