# Prolific survey api 

[![Build Status](https://travis-ci.org/dev-11/prolific-surveys-api.svg?branch=master)](https://travis-ci.org/dev-11/prolific-surveys-api)
[![codecov](https://codecov.io/gh/dev-11/prolific-surveys-api/branch/master/graph/badge.svg)](https://codecov.io/gh/dev-11/prolific-surveys-api)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0971683aad8c4d898d2c11f45e1768b8)](https://www.codacy.com/manual/dev-11/prolific-surveys-api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dev-11/prolific-surveys-api&amp;utm_campaign=Badge_Grade)

## Solution

The solution uses two services and two repositories.

## Repositories

The `SurveyRepository` and the `SurveyResponseService` handles every data storage related operation, in a separated responsibility fashion. They don't hold any business logic, they just read, update, store the data.  

## Services

The `SurveyService` communicates with its repository and also implements the business logic, like telling the `SurveyReposity` to update the `available places` property.  
The `SurveyResponseService` handles every business logic related to the responses to a survey.

## APIs

The system recognises two namespaces `surveys` and `survey-responses` they expose their service related to the actual namespace.

## Improvements

The repositories store everything at the memory, for a production ready solution that has to change. 
There is no data validation at the endpoints, users can send in 0 for as the value of the user_id, or an empty string for the survey name, etc.
There is no consolidated error handling in the api or standardized response format. I would return a format like this:
```json5
{
  "statusCode": 200,
  "body": {
    // ... the payload goes here
  }
}
```

## How to run

The solution has two dependencies which can be resolved by the `pip install -r requirements.txt` command, ideally in a venv.
This command will start the app:
```bash
python3 app.py
```

The application exposes a swagger documentation page at the [http://127.0.0.1:5005/doc/](http://127.0.0.1:5005/doc/) endpoint.
