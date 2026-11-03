import http.server
import socketserver
import webbrowser

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"TripWise chalu zala! Browser madhe he ughad: http://localhost:{PORT}")
    webbrowser.open(f"http://localhost:{PORT}")
    httpd.serve_forever()