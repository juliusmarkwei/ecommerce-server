FROM python:3.10

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev
    
ENV PIP_DISABLE_PIP_VERSION_CHECK 1 
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./requirements/development.txt .

RUN set -ex \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r development.txt

COPY . .

EXPOSE 8000

CMD ["python3", "manage.py", "runserver"]