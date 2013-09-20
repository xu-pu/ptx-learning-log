#!/usr/bin/env python3

import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

web_dir = '/home/sheep/Dropbox/code/random-tests/pyhttp/'
port = 80

os.chdir(web_dir)
server_addr = ('localhost', port) 
server_obj  = HTTPServer(server_addr, CGIHTTPRequestHandler)
server_obj.serve_forever()
