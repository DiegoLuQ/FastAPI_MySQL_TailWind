FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app_d

COPY ./app/requirements.txt /app_d/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app_d/requirements.txt

COPY ./app /app_d/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

