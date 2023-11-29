from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "10.0.0.35"
PORT = 5000

class RequestHandler(BaseHTTPRequestHandler): #custom request handler, inherits from basehttprequesthandler
    def do_POST(self): #method to handle post request
        content_length = int(self.headers["Content-Length"]) #extract content length from request headers
        post_data = self.rfile.read(content_length) #read post data from request
        data = json.loads(post_data.decode("utf-8")) #decode and parse received JSON data 

        if self.path == "/api/v2/lightstatus":
            print("Received data from Smart LED Light:", data)

        if self.path == "/api/v2/smartwatch":
            print("Received data from Smartwatch:", data)

        self.send_response(200) #send succesfull status code
        self.send_header("Content-type","application/json") #set content type as json in response header
        self.end_headers()
        response = json.dumps({"message": "Data received succesfully"}) #create the json response message
        self.wfile.write(response.encode("utf-8")) #write the json message to client

def run_server():
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address,RequestHandler) #create http server object with defined address and request handler
    print(f"Server running on {HOST}:{PORT}") 

    try:
        httpd.serve_forever() #start serving incoming http requests 
    except KeyboardInterrupt: #crtl+c
        print("Stopping the server")
        httpd.server_close()
if __name__ == "__main__":
    run_server()