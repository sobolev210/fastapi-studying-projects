FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY ./requirements.txt /code

RUN pip install --no-cache-dir --upgrade -r requirements.txt

# maybe make it as one COPY instruction
COPY ./app /code/app

COPY ./alembic /code/alembic

COPY ./alembic.ini /code

COPY ./docker-entrypoint.sh /code

# как будто работает, если БД запущена во время сборки образа. Если не запущена - ошибка
# RUN alembic upgrade head
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]

CMD ["sh", "docker-entrypoint.sh"]
