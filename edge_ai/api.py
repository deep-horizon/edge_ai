import os
import requests
import json


class Api:

  def __init__(self, app_secret=None):
    self.app_secret = app_secret
    base_url = os.environ.get('EDGE_AI_URL') or 'https://www.edgeai.io'

    if base_url.endswith('/'):
      base_url = base_url[:-1]

    self.url = base_url + '/api'

  def get(self, path, args={}):
    return self.request('get', path, args)

  def post(self, path, args={}):
    return self.request('post', path, args)

  def put(self, path, args={}):
    return self.request('put', path, args)

  def delete(self, path, args={}):
    return self.request('delete', path, args)

  def request(self, method, path, args={}):
    if not self.app_secret:
      raise StandardError('EdgeAI client not fully configured. Make sure app_token and app_secret '
                          'are BOTH provided during client instantiation or as environment variables '
                          'EDGE_AI_TOKEN and EDGE_AI_SECRET, respectively.')

    func = getattr(requests, method)

    headers = {'EdgeAI-Token': self.app_secret}

    if method in ['post', 'put']:
      resp = func(self.url + path, json=args, headers=headers)
    else:
      resp = func(self.url + path, data=args, headers=headers)

    try:
      resp_body = json.loads(resp.content)
    except:
      resp_body = {'ok': False, 'error': 'unknown_error'}

    return resp_body