from http.server import BaseHTTPRequestHandler,HTTPServer
import json, os

PORT_NUMBER = 5000

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == "":
            self.path = "/index.html"
        try:
            sendReply = False
            if self.path.endswith(".html"):
                mimetype = "text/html"
                sendReply = True
            if self.path.endswith(".json"):
                mimetype = "text/plain"
                sendReply = True
            if self.path.endswith(".js"):
                mimetype = "application/javascript"
                sendReply = True
            if self.path.endswith(".png"):
                mimetype = "image/png"
                sendReply = True
            if self.path.endswith(".css"):
                mimetype = "text/css"
                sendReply = True
            if self.path.endswith(".ico"):
                mimetype = "image/icon"
                sendReply = True
            if self.path.endswith(".svg"):
                mimetype = "image/svg+xml"
                sendReply = True
            if self.path.endswith(".glsl"):
                mimetype = "text/palin"
                sendReply = True
            if self.path.endswith(".obj"):
                mimetype = "text/plain"
                sendReply = True
            if self.path.endswith(".mtl"):
                mimetype = "text/plain"
                sendReply = True
            if self.path.endswith(".bmp"):
                mimetype = "image/bmp"
                sendReply = True

            if sendReply:
                f = open("." + self.path, "rb")
                self.send_response(200)
                self.send_header("Content-type", mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            return
        except IOError:
            self.send_error(404, "File Not Found: " + self.path)

    def do_POST(self):
        pass

try:
    server = HTTPServer(("", PORT_NUMBER), Handler)
    server.serve_forever()
except KeyboardInterrupt:
    server.socket.close()
