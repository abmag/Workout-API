# Overview

I decided to make this project using Flask because I wanted to try backend development in python.
I decided early on that I would try to make a full-stack application, so I used Flask's Blueprints feature to separate front end views from api calls.

To run and test this api, clone the repo, install all dependencies, and then initialize the database with 
`flask --app flaskr init-db`
Then start the server with 
` flask --app flaskr run --debug`
and you will be able to make api calls with an app like postman.


# Documentation

## Endpoints

### /api/workouts/

This endpoint is used for querying entries. 
#### GET
- Used to query the database
##### Expected Output 
- A list of JSON objects representing all workouts that match the request filters.
##### Optional Parameters
A JSON object that contains one or more of the following:

- average_heart_rate - integer value
- date_time - timestamp notation, ex. 2024-01-01 01:00:00
- distance - integer value in kilometers
- duration - integer value in minutes
- id - the internal id for each workout used by the database
- max_heart_rate - integer value
- route_nickname - string value

### /api/create/

This endpoint is used for posting to the database.

#### POST
- Add a workout to the database
#### Expected Output
- A list of JSON objects representing all workouts, with the new workout added
#### Required Parameters
A JSON object that contains the following:

- distance - integer value in kilometers
- duration - integer value in minutes

#### Optional Parameters
- average_heart_rate - integer value
- date_time - timestamp notation, ex. 2024-01-01 01:00:00
- max_heart_rate - integer value
- route_nickname - string value

### api/<int:id>/update/

This endpoint is used for editing an entry in the database at the given id

#### PUT
- Replace the workout at the specified id with updated information from a JSON formatted request
#### Expected Output
- A list of JSON objects representing all workouts, with the new data entered
#### Required Parameters
A JSON object that contains all of the following:

- average_heart_rate - integer value
- date_time - timestamp notation, ex. 2024-01-01 01:00:00
- distance - integer value in kilometers
- duration - integer value in minutes
- max_heart_rate - integer value
- route_nickname - string value


### api/<int:id>/delete/

This endpoint is used for deleting an entry in the database

#### DELETE
- Delete the workout at the given id and remove it from the database
#### Expected Output
- A list of JSON objects representing all workouts after the deletion
#### Parameters
- No parameters expected
