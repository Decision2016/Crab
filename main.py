# coding:utf-8

import json
import photoCut
from wsgiref.simple_server import make_server
from gevent import pywsgi

keyfile = ''
certfile = ''

def application(env, start_response):
    if env['PATH_INFO'] == '/':
        start_response('200 OK', [('Content-Type', 'application/json')])
        request_body = env["wsgi.input"].read(int(env.get("CONTENT_LENGTH", 0)))
        request_body = json.loads(request_body)
        base64code = request_body["base64code"]
        array = request_body["array"]
        dic = photoCut.photocut(array, base64code)

        return [json.dumps(dic).encode('utf-8')]
    else:
        start_response('200 OK', [('Content-Type', 'application/json')])
        dic = {
            'errMsg': '404 Not Found'
        }
        return [json.dumps(dic).encode('utf-8')]

if __name__ == "__main__":
    port = 23333
    server = pywsgi.WSGIServer(('0.0.0.0', port), application, keyfile=keyfile, certfile=certfile)
    print("serving http on port {0}...".format(str(port)))
    server.serve_forever()
