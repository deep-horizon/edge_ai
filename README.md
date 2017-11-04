# Python EdgeAI API Client

## Requirements
- Python >= 2.7

## Installation

Via pip
```
$ pip install edge_ai
```

## Usage

**Client Configuration**

```python
from edge_ai import EdgeAI

edge_ai_client = EdgeAI(
  app_token='<YOUR_APP_TOKEN>',
  app_secret='<YOUR_APP_SECRET>'
)
```

If not provided upon client instantiation, `app_token` and `app_secret` will be set to the following environment variables, respectively:
```
EDGEAI_TOKEN
EDGEAI_SECRET
```

**Fetching Predictions**

Getting a prediction via the client can be done safely in the following manner:
```python
# dict of input features required to make a prediction with your model
features = {
  'some_feature': 'some_value'
}

resp = edge_ai_client.predict(features)

if resp.get('ok'):
  prediction = resp['prediction']
  print('Got Prediction: {}'.format(prediction))
else:
  err = resp['error']
  print('Prediction Error: {}'.format(err))
```

The response payload for fetching predictions is represented by the following JSON format:
```python
{
  "ok": True,
  "prediction": "<some_prediction>"
}
```

If an error is encountered, the format will look like this instead:
```python
{
  "ok": False,
  "error": "<error_name>"
}
```

**Errors**

The following errors may be returned while fetching a prediction:

Name | Description
--- | ---
`not_authorized` | API request has invalid authorization. Ensure app token and app secret are valid.
`no_features_provided` | `predict` request had no provided features to make prediction with.
`required_features_missing` | One or more features required to make a prediction was not provided in the API request
`prediction_error` | Error while making prediction for provided features. Ensure all required features were provided during request. 
`unknown_error` | Unknown error response from API. Response not in expected format.

## License

MIT