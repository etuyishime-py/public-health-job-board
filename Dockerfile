FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt gunicorn

CMD python init_db.py && gunicorn -b 0.0.0.0:5000 app:app

