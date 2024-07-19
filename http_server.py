from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
import socketserver
import time

hostname = 'localhost'
serverport = 8080

class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'Input.html'
        return SimpleHTTPRequestHandler.do_GET(self)
    
    
handler_object = RequestHandler

my_server = socketserver.TCPServer(("", serverport), handler_object)
my_server.serve_forever()
