import json

import os
from apistar import App, Route, http


def welcome():
  return {'hello': 'world'}

def data_fetcher(accept_language: http.Header) -> http.JSONResponse:

    headers = {'Content-Type': 'application/json',
               'Access-Control-Allow-Origin': '*'}
    # TODO: check if this Access-Control definition is the best approach, since it may leave the app insecure

    filename = "data.json"
    with open(os.path.join(BASE_DIR, filename)) as f:
        jsonarray = json.load(f)
    return http.JSONResponse(jsonarray, status_code=200, headers=headers)

BASE_DIR = os.path.dirname(__file__)

routes = [
    Route('/', method='GET', handler=welcome),
    Route('/data', method='GET', handler=data_fetcher),
]

app = App(routes=routes, schema_url='/schema/', docs_url='/docs/')

if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True)

