import os
from api import Api


class EdgeAI:

  def __init__(self, app_token=None, app_secret=None):
    self.app_token = app_token or os.environ.get('EDGEAI_TOKEN')
    self.app_secret = app_secret or os.environ.get('EDGEAI_SECRET')

    self.api = Api(self.app_secret)

  def predict(self, features=None):
    payload = {
      'features': features or {},
      'app_token': self.app_token
    }

    return self.api.post('/predict', payload)