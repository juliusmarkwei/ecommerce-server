FROM python:3.10

ENV PIP_DISABLE_PIP_VERSION_CHECK 1 
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./requirements/development.txt .

RUN pip install -r development.txt

COPY . .

EXPOSE 8000

CMD ["python3", "manage.py", "runserver"]