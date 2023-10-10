from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

PORT = 5310
DIRECTORY = '/path/to/your/directory'

handler = SimpleHTTPRequestHandler
httpd = TCPServer(("", PORT), handler)
httpd.allow_reuse_address = True  # 

print(f"Serving directory '{DIRECTORY}' at port {PORT}")
httpd.serve_forever()
