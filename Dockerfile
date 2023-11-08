FROM python:3.11-slim

WORKDIR /opt/todolist-django

ENV PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_NO_CACHE_DIR=off \
    PYTHON_PATH=/opt/todolist-django

RUN groupadd --system service && useradd --system -g service api

RUN pip install "poetry==1.4.2"

COPY poetry.lock ./
COPY pyproject.toml ./

RUN poetry config virtualenvs.create false && poetry install --no-ansi

COPY src/ ./

USER api

ENTRYPOINT ["bash", "entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
