import datetime
import json

from apistar import App, Route, http
from apistar.codecs import JSONCodec

from LineToPlot import LineToPlot


def welcome(name = None):
  if name is None:
    return {'message': 'welcome to api star'}
  return {'message': 'welcome to api star, %s' %(name)}

def data_fetcher():
        codec = JSONCodec()
        content = codec.decode('{"name": "john"}')
        headers = {'Content-Type': 'application/json'}
        return http.Response(content, headers=headers)

def hello_world(accept_language: http.Header) -> http.JSONResponse:

    #data = {'text': 'Hello, world!'}
    #return http.JSONResponse([data]*3, status_code=200)
    headers = {'Content-Type': 'application/json',
               'Access-Control-Allow-Origin': '*'}
    # TODO: check if this Access-Control definition is the best approach, since it may leave the app insecure

    filename = "C:\\Users\\d91421\\Code\\prototype-finance\\python-backend\\data.json"
    with open(filename) as f:
        jsonarray = json.load(f)
    return http.JSONResponse(jsonarray, status_code=200, headers=headers)

routes = [
    Route('/', method='GET', handler=welcome),
Route('/data', method='GET', handler=hello_world),
]

genesis_block = LineToPlot(name="oi", series= [])
the_blockchain = [genesis_block]
current_state = genesis_block

app = App(routes=routes)

if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True)

