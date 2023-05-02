## Introduction
This is a simple Flask application that allows users to upload and manage configuration files.

## Requirements
- Python 3
- Flask
- pymongo

## Installation
**Install dependencies using pip install -r requirements.txt. Start the application using python app.py.**


## Endpoints
- ***/upload***

Request
Method: POST
Body: JSON data containing configuration information
Response
Status Code:
302 if the configuration was successfully uploaded and the user is redirected to the homepage.
400 if the input data is invalid.
500 if there was an error saving the configuration to the database.
/
Request
Method: GET
Response
Renders the homepage template and a list of all configurations.
/configs
Request
Method: GET
Response
Renders the configuration list template and a list of all configurations.
/configs/<config_id>
Request
Method: GET
URL Parameter: <config_id> (the ID of the configuration to be retrieved)
Response
Renders the configuration template and displays the requested configuration.
Request
Method: DELETE
URL Parameter: <config_id> (the ID of the configuration to be deleted)
Response
Status Code:
200 if the configuration was successfully deleted.
404 if the requested configuration is not found.
