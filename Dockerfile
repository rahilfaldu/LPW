
FROM python:3.9-slim


ENV PYTHONUNBUFFERED 1


WORKDIR /app


COPY requirements.txt /app/


RUN pip install -r requirements.txt


COPY . /app/


EXPOSE 5000


CMD ["python", "HMS.py"]