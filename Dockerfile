FROM python:3.13-slim
LABEL authors="ruslana"

WORKDIR /app
COPY pyproject.toml poetry.lock .env /app/

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root

COPY contacts_api /app/contacts_api



EXPOSE 8000

CMD ["uvicorn", "contacts_api.app.main:app", "--host", "0.0.0.0", "--port", "8000"]