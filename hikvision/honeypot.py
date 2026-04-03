#!/usr/bin/env python3
"""
CVE-2017-7921 Hikvision Honeypot
Simple, clean implementation
"""
from http.server import HTTPServer, BaseHTTPRequestHandler

class HikvisionHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        print(f"[+] {self.address_string()} - {format % args}")
    
    def do_GET(self):
        # CVE-2017-7921: Authentication bypass
        if '/Security/users' in self.path:
            self.send_response(200)
            self.send_header('Content-type', 'application/xml')
            self.end_headers()
            xml = '''<?xml version="1.0" encoding="UTF-8"?>
<UserList version="1.0" xmlns="http://www.hikvision.com/ver20/XMLSchema">
    <User version="1.0">
        <id>1</id>
        <userName>admin</userName>
        <password>YWRtaW46MTIzNDU=</password>
        <userLevel>Administrator</userLevel>
    </User>
    <User version="1.0">
        <id>2</id>
        <userName>operator</userName>
        <password>b3BlcmF0b3I6b3BlcmF0b3I=</password>
        <userLevel>Operator</userLevel>
    </User>
</UserList>'''
            self.wfile.write(xml.encode())
            print(f"[!] CVE-2017-7921 exploited by {self.address_string()}")
        
        # Configuration file download
        elif '/System/configurationFile' in self.path:
            self.send_response(200)
            self.send_header('Content-type', 'application/xml')
            self.end_headers()
            xml = '''<?xml version="1.0" encoding="UTF-8"?>
<ConfigurationData version="1.0" xmlns="http://www.hikvision.com/ver20/XMLSchema">
    <DeviceInfo>
        <deviceName>IPCamera</deviceName>
        <model>DS-2CD2032-I</model>
        <firmwareVersion>V5.2.0 build 140721</firmwareVersion>
    </DeviceInfo>
    <Security>
        <adminPassword>12345</adminPassword>
        <operatorPassword>operator</operatorPassword>
    </Security>
</ConfigurationData>'''
            self.wfile.write(xml.encode())
            print(f"[!] Config file downloaded by {self.address_string()}")
        
        # Default page
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = b'''<html>
<head><title>Hikvision IP Camera</title></head>
<body>
    <h2>Hikvision DS-2CD2032-I</h2>
    <p>Model: DS-2CD2032-I</p>
    <p>Firmware: V5.2.0 build 140721</p>
</body>
</html>'''
            self.wfile.write(html)

if __name__ == '__main__':
    print('[+] CVE-2017-7921 Hikvision Honeypot')
    print('[+] Listening on http://0.0.0.0:8080')
    print('[+] Press Ctrl+C to stop\n')
    
    server = HTTPServer(('0.0.0.0', 8080), HikvisionHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\n[*] Shutting down...')
        server.shutdown()
