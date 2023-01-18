FROM nginx/unit:1.23.0-python3.9

WORKDIR /app_d

COPY ./app/requirements.txt /app_d/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app_d/requirements.txt

COPY ./app /app_d/

