FROM python:3.10

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PORT=8000

ADD . /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD gunicorn impact.wsgi:application --bind 0.0.0.0:$PORT