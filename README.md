  &#xa0;

<h1 align="center">IGS Django Coding Test</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/anolivei/IGS?color=3de069">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/anolivei/IGS?color=3de069">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/anolivei/IGS?color=3de069">

  <img alt="License" src="https://img.shields.io/github/license/anolivei/IGS?color=3de069">

  <img alt="Pep8" src="https://github.com/anolivei/IGS/actions/workflows/pep8.yml/badge.svg?event=push">

</p>

<p align="center">
  <a href="#about">About</a> &#xa0; | &#xa0;
  <a href="#about">Problem</a> &#xa0; | &#xa0;
  <a href="#about">Deliverables</a> &#xa0; | &#xa0;
  <a href="#technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#starting">Starting</a> &#xa0; | &#xa0;
  <a href="#license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/anolivei" target="_blank">Author</a>
</p>

<br>

## About ##

The purpose of this coding test is to evaluate my skills using Python
and the Django web framework.

## Problem ##

The IGS team is growing every month and now they need to have some applications
to manage employee information, such as name, e-mail and department.
As any application written at IGS, It must have an API to allow integrations.

## Deliverables ##

"IGS-Software Manager" app must have:

● A django admin panel to manage employees's data.

● A Django API to list, add and remove employees.

● the code should be delivered to a github.com repository.

## Technologies ##

The following tools were used in this project:

- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/)

## Requirements ##

Before starting, you need to have [Git](https://git-scm.com) and ([Python 3.9.5](https://www.python.org/) or [docker](https://www.docker.com/)) installed.
## Starting ##

You can start this project in two ways:

First way ([Python 3.9.5](https://www.python.org/) required)

```bash
# Install Python 3.9.5 and pip

# Clone this project
git clone https://github.com/anolivei/IGS

# Access
cd IGS/IGS-Software-Manager

# Install the project requirements
pip install -r requirements.txt

# Run the project
python3 manage.py runserver

# The server will initialize in the <http://localhost:8000>
# The list of employees in the <http://localhost:8000/employee/>
# The admin system in the <http://localhost:8000/igs/>
```

Second way ([Docker](https://docs.docker.com/get-started/) and [docker-compose](https://docs.docker.com/compose/install/) required)

```bash
# Install Docker and docker-compose

# Clone this project
git clone https://github.com/anolivei/IGS

# Access
cd IGS

# docker-compose up
docker-compose up --build -d

# The server will initialize in the <http://localhost:8000>
# The list of employees in the <http://localhost:8000/employee/>
# The admin system in the <http://localhost:8000/igs/>
```

username: user

password: user

## License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE) file.


&#xa0;

<a href="#top">Back to top</a>
