from http.server import BaseHTTPRequestHandler
from urllib import parse 
from logic.functions import morse_code


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        '''A function that send request to vercel'''
        s=self.path
        url_components=parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dictionary=dict(query_string_list)

        if 'code' in dictionary:
            text_to_code = dictionary['code']
            coded_text =  morse_code(text_to_code) 
            message = f"Your Coded Message...\n{coded_text}"

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
     
        self.wfile.write(message.encode())
        return