# coding:utf-8

import json
import photoCut
from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])

    request_body = environ["wsgi.input"].read(int(environ.get("CONTENT_LENGTH", 0)))
    request_body = json.loads(request_body)
    base64code = request_body["base64code"]
    array = request_body["array"]

    dic = photoCut.photoCut(array, base64code)

    return [json.dumps(dic).encode('utf-8')]

if __name__ == "__main__":
    port = 8080
    httpd = make_server("127.0.0.1", port, application)
    print("serving http on port {0}...".format(str(port)))
    httpd.serve_forever()