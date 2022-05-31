from http.server import BaseHTTPRequestHandler, HTTPServer

APP_HOST = "localhost"
APP_PORT = 8080

class SimpleGetHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    def _html(self, message):
        content = (f"<html>"
                   f"<body>"
                   f"<h1>{message}</h1>"
                   f"</body>"
                   f"</html>"
                   )
        return content.encode("utf-8")
    def do_GET(self):
        self._set_headers()
        message = "Hello world!"
        self.wfile.write(self._html(message))

def run_server(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_adress = (APP_HOST, APP_PORT)
    httpd = server_class(server_adress, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    run_server(handler_class=SimpleGetHandler)