
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

def predict_result(internal_marks, attendance):
    if internal_marks >= 40 and attendance >= 75:
        return "PASS"
    return "FAIL"

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            result = predict_result(70, 85)
            response = {
                "project": "first-ci-demo",
                "predicted_result": result,
                "status": "running"
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        print(format % args)

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", int(__import__("os").environ.get("PORT", 10000))), RequestHandler)
    print("Server running...")
    server.serve_forever()
