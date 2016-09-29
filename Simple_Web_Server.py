import http.server
import socketserver

PORT = 9099

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("/home/", PORT), Handler)

print("Serving at port", PORT)
httpd.serve_forever()