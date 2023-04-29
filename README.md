# NYC COMPOSTS  

[![Python Version](https://img.shields.io/badge/python-3.7-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.2-brightgreen.svg)](https://djangoproject.com)
  
## Dev-branch  
[![Build Status](https://app.travis-ci.com/gcivil-nyu-org/INET-Monday-Spring2023-Team-4.svg?branch=develop)](https://app.travis-ci.com/gcivil-nyu-org/INET-Monday-Spring2023-Team-4)
[![Coverage Status](https://coveralls.io/repos/github/gcivil-nyu-org/INET-Monday-Spring2023-Team-4/badge.svg?branch=develop)](https://coveralls.io/github/gcivil-nyu-org/INET-Monday-Spring2023-Team-4?branch=develop)
  
  
## Prod-branch  
[![Build Status](https://app.travis-ci.com/gcivil-nyu-org/INET-Monday-Spring2023-Team-4.svg?branch=main)](https://app.travis-ci.com/gcivil-nyu-org/INET-Monday-Spring2023-Team-4)
[![Coverage Status](https://coveralls.io/repos/github/gcivil-nyu-org/INET-Monday-Spring2023-Team-4/badge.svg?branch=main)](https://coveralls.io/github/gcivil-nyu-org/INET-Monday-Spring2023-Team-4?branch=main)
  
Step-1
Clone the Repo

Step-2
Follow below commands 

$ pip install -r requirements.txt

$ python manage.py migrate

$ python manage.py loaddata fixtures/*.json

$ python manage.py createsuperuser

$ python manage.py setup

$ python manage.py runserver
