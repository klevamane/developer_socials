# Developer Social
A place where developers can view profiles and get information about each other

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

Prerequisites
```
- Python 3.6+
- Django
- djangorestframework 2.0+
- pipenv

```
- git clone https://github.com/klevamane/developer_socials
- cd developer_socials
- pipenv install
- create a database in postgresql with your desired name and password
- update the .env file
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

Note you can make create a super user by **python manae.py createsuperuser**

## Running the tests
From the terminal run **pytest**

## Deployment
Add additional notes about how to deploy this on a live system

## Built With
Django - The web framework used
Postgres - The database used

## Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning
We use SemVer for versioning. For the versions available, see the tags on this repository.

## Authors
Onengiye Richard - Initial work - PurpleBooth


## License
This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments
Onengi
