from http.server import HTTPServer, BaseHTTPRequestHandler

content = """ 
<html>
    <head>
        <title>My Web Server</title>
        <style>
            body {
                background-color: white;
                color: black;
                font-family: 'Times New Roman', serif;
            }
            h2 {
                text-align: center;
                text-decoration: underline;
            }
            table {
                border-collapse: collapse;
                width: 70%;
                margin: auto;
                background-color: #00bfff;
            }
            th, td {
                border: 1px solid black;
                text-align: center;
                padding: 15px;
            }
            th {
                background-color: #00bfff;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <h2>LIST OF PROTOCOLS IN TCP AND IP PROTOCOL SUITE</h2>

        <table>
            <tr>
                <th>S.NO</th>
                <th>Name of the Layer</th>
                <th>List of Protocols</th>
            </tr>
            <tr>
                <td>1.</td>
                <td>Application Layer</td>
                <td>HTTP, FTP, DNS, Telnet, SSH</td>
            </tr>
            <tr>
                <td>2.</td>
                <td>Transport Layer</td>
                <td>TCP, UDP</td>
            </tr>
            <tr>
                <td>3.</td>
                <td>Network Layer</td>
                <td>Ethernet</td>
            </tr>
            <tr>
                <td>4.</td>
                <td>Data Link Layer</td>
                <td>TCP and UDP</td>
            </tr>
        </table>
    </body>
</html>
"""

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET request received...")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver")
server_address = ('', 8000)
httpd = HTTPServer(server_address, MyServer)
httpd.serve_forever()