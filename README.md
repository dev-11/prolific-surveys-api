# Prolific survey api 

[![Build Status](https://travis-ci.com/dev-11/prolific-surveys-api.svg?branch=master)](https://travis-ci.com/dev-11/prolific-surveys-api)
[![codecov](https://codecov.io/gh/dev-11/prolific-surveys-api/branch/master/graph/badge.svg)](https://codecov.io/gh/dev-11/prolific-surveys-api)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0971683aad8c4d898d2c11f45e1768b8)](https://www.codacy.com/manual/dev-11/prolific-surveys-api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dev-11/prolific-surveys-api&amp;utm_campaign=Badge_Grade)

## Solution

The solution uses two services and two repositories.

## Repositories

The `SurveyRepository` and the `SurveyResponseService` handle every data storage related operation, in a separated responsibility fashion. They don't hold any business logic, they just read, update, or store the data.  

## Services

The `SurveyService` communicates with its repository and also implements the business logic, like telling the `SurveyReposity` to update the `available places` property.  
The `SurveyResponseService` handles every business logic related to the responses to a survey.

## APIs

The api recognises two namespaces `surveys` and `survey-responses` they expose their service related to the actual namespace.

## Improvements

The repositories store everything in the memory, for a production ready solution that has to change. 
There is no data validation at the endpoints, users can send in 0 as the value of the user_id, or an empty string for the survey name, etc.
There is no consolidated error handling in the api or standardized response format. I would return a format like this:
```json5
{
  "statusCode": 200,
  "body": {
    // ... the payload goes here
  }
}
```
Because of the separation there is no direct link between the survey and the survey responses, if there is a persistence layer to be introduced then a merged storage of the two entities would be better. This separation looked a good solution when I wrote the code, if I could do it again, I would probably choose the format below, with lazy loading to avoid reading up a million responses when we just need to update the `available_places` property. For example:
```json5
{
  "id": "8f5454ed-8fe5-430a-97ad-c8dc424eda6a",
  "survey name": "Are you a dog person or a cat person?",
  "available places": 256,
  "user_id": 27,
  "responses": [
    {
      "id": "0f773e3d-9ef4-47ba-95bc-45db2c553a24",
      "user_id": 1024
    },
    {
      "id": "3a3b9488-de64-4c56-87d2-21c5bc76a253",
      "user_id": 2048
    }
  ]
}
``` 

## How to run

The solution has two dependencies which can be resolved by the `pip install -r requirements.txt` command, ideally in a venv.
This command will start the app:
```bash
python3 app.py
```

The application exposes a swagger documentation page at the [http://127.0.0.1:5005/doc/](http://127.0.0.1:5005/doc/) endpoint.
