#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import paho.mqtt.publish as publish
from subprocess import check_output
from re import findall
import psutil
import sys

hostName = "sirius.vrdaf.org"
serverPort = 8081
clientaddr =""

def publish_message(topic, message):
    #print("Publishing to MQTT topic: " + topic)
    #print("Message: " + message)

    publish.single(topic, message, hostname="192.168.0.77")
    
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)        
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>NATO SENSOR</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is the NATO IDS.</p>", "utf-8"))
        self.wfile.write(bytes("<p>You are not NATO.</p>", "utf-8"))
        self.wfile.write(bytes("<p>Launching Countermeasuers against %s.</p>"% self.address_string(), "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        publish_message("M9",self.address_string())
    def ShowClient(self):
        clientaddr=self.address_string()
        

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    #Myserver.ShowClient()
    print(clientaddr)
    

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
