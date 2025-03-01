FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir fastapi uvicorn

EXPOSE 8000

CMD ["uvicorn", "src:app", "--host", "0.0.0.0", "--port", "8000"]
