# Casting Agency API

This application manages Casting Agency's backend. It has two main entities ```Actors``` and ```Movies```. Users of this application can create, update, read and delete actors and movies.

### Users
This app has 3 roles and 3 users. The token for each of the users are mentioned in `setup.sh` file. Details about each user privilege are provided below.

- Casting Assistant
	- Can view actors and movies

- Casting Director
	- All permissions of a Casting Assistant and
	- Add or delete an actor from the database
	- Modify actors or movies

- Executive Producer
	- All permissions of a Casting Director and
	- Add or delete a movie from the database

### Endpoints

- GET '/actors'
- GET '/movies'
- POST '/actors'
- POST '/movies'
- PATCH '/actors/<int:id>'
- PATCH '/movies/<int:id>'
- DELETE '/actors/<int:id>'
- DELETE '/movies/<int:id>'



## Getting Started
This project uses python, flask and postgresql for it's backend and is hosted on Heroku.

### Installing Dependencies

#### Python 3.7

#### Virtual Enviornment

Instructions for setting up a virtual environment can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all the required packages to run this app.


## Running the server


To run the server locally, execute below commands from your vurtual ennvironment:

```bash
source setup.sh
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
Sourcing `setup.sh` sets tokens and database paths used by the app.

The application is hosted on heroku @ https://capstone-test-abagaria.herokuapp.com

## Testing

To run the tests, from the root folder, run
```
./execute_test.sh
```

## Deployment
The app is deployed on Heroku https://capstone-test-abagaria.herokuapp.com.


