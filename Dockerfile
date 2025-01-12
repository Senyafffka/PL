FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir pytz && \
pip install --no-cache-dir requests && \
pip install --no-cache-dir tzlocal

COPY app.py app.py
COPY test.py test.py

EXPOSE 8000

CMD ["python", "app.py"]
