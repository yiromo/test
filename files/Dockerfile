FROM python:3.11.9-bookworm

WORKDIR /test

COPY requirements.txt .
COPY ./src ./src

RUN pip install -r requirements.txt

CMD ["python", "./src/main.py"]
