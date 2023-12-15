# Ecommerce Backend build with Django Rest Framework

<a href="https://www.django-rest-framework.org/" target="_blank">
    <img src="./assets/others/django drf logo.png" height=150px width=100% >
</a>

## A fully functional Ecommerce - Django Rest API project build and tested with <a href="https://www.django-rest-framework.org/" target="_blank">restframework</a> and deployed to <a href="https://vercel.com/" target="_blank">vercel</a>

The project was inspired by a random database schema of an ecommerce website I found on <a href="https://azimutt.app/gallery/e-commerce">Azimutt gallery</a>. Every piece of this project required alot of time and research since it was one of my beginner projects build in django. The activities involved in this project are as follows:

1. Database model (table) development development and configurations
2. Writing the various API views for all the neccessary methods of each view
3. Admin panel management configurations.
4. Adding all the neccesary URL endpoints to for all the various views and thier methods. Not fogetting the admin panel too.
5. Writing tests for all the views and thier methods. I also used Postman for testing as well.
5. Including a <a href="https://ecommerce-backend-4el9fq6v0-julius-markweis-projects.vercel.app/" target="_blank">documentation</a> for the project through a python module called <a href="https://pypi.org/project/openapi3/" target="_blank">drf-yash</a> by <a href="https://www.openapis.org/" target="_blank">OpenAPI Initiative</a>.
5. Dockerized the Django Rest API whci I was able to successfully run on my local machine.
6. Deploy the Django REST API to <a href="https://vercel.com/" target="_blank">vercel</a>

## Prerequisites
```
    python3.10
    django
    djanfo-restframework
    docker (*optional)
```

## Installation
1. #### Clone this repository
```
    git clone https://github.com/juliusmarkwei/ecommerce-backend.git
    cd ecommerce-backend/
```
2. #### Install all the neccessary packages/dependencies
```
    pip install -r requirements.txt
```
3. In the root directory of the project, create a superuser to manage all the users of the application. be sure python is installed before you proceed with this stage.
```
    python3 manage createsuperuser
```
4. #### Run the program with the following command
```
    python3 manage runserver
```

## Run the program using <a href="https://www.docker.com/" target="_blank">Docker</a> 
Docker and Docker Compose should be installed on your system. For Docker installation guide: <a href="https://docs.docker.com/get-docker/" target="_blank">Get Docker</a> and <a href="https://docs.docker.com/compose/install/" target="_blank">Install Docker Compose</a>. Steps to run the application:

1. #### Clone the Repository
```
    git clone https://github.com/juliusmarkwei/ecommerce-backend.git
    cd ecommerce-backend/
```
2. #### Environment Variables
* Create a <strong>`.env`</strong> preferrably in <strong>/main/settings/</strong>. Inside the <strong>.env</strong> add a SECRET_KEY and your database configurations of the database of your choice. You can generate a <strong>`SECRET_KEY`</strong> using the following code snippet:
```
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
```

* Add the following line printed above to the <strong>`.env`</strong> file:
```
    SECRET_KEY=your_secret_key_here
    DB_HOST=your_db_host
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_NAME=your_db_name
    DB_PORT=your_db_port
    DB_ENGINE=your_db_engine
```
3. #### Build and Run with Docker Compose
```
    docker-compose up --build
```
* This command builds the Docker image starts the containers as defined in the docker-compose.yml file.

4. #### Access the Application
* Once the application (container) is running, access the application running on port 8000 via http://localhost:8000.

5. #### Additional Commands
* Stopping the application: <strong>`docker-compose down`</strong>
* Rebuilding the application after changes: <strong>`docker-compose up --build`</strong>

