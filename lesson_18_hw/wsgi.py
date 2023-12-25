from wsgiref.simple_server import make_server


def making_server(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response(status, headers)
    return [b"Bip-bip - machine's sound"]


with make_server('', 8000, making_server) as server:
    print("Server is  http://localhost:8000...")
    server.serve_forever()
