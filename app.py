import os
from base_page import BasePage
from generate_sniper_pdf import generate_sniper_pdf

STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')

def application(environ, start_response):
    path = environ.get('PATH_INFO', '/')
    status = '200 OK'
    response_body = b'Path not found'

    try:
        if path == '/api/sniper':
            if environ['REQUEST_METHOD'] == 'OPTIONS':
                response_body = b''
            elif environ['REQUEST_METHOD'] == 'POST':
                content_length = int(environ.get('CONTENT_LENGTH', 0))
                request_body = environ['wsgi.input'].read(content_length)
                decoded_body = request_body.decode('utf-8')
                pdf_data = generate_sniper_pdf(decoded_body)
                response_body = pdf_data
            else:
                response_body = b"This endpoint is ready to receive a POST request."
        
        elif path == '/api/':
            response_body = b"Working"
        
        elif path == '/':
            page = BasePage("Eduardo Osteicoechea")
            response_body = page.html().encode('utf-8')
            
        elif path == '/article':
            page = BasePage("Artículos", ["article"], ["article"], True)
            response_body = page.html().encode('utf-8')
            
        elif path == '/songs':
            page = BasePage("Cánticos", ["article", "songs"], ["songs"], True)
            response_body = page.html().encode('utf-8')
        
        else:
            status = '404 Not Found'
            response_body = b'Path not found'
            
    except Exception as e:
        status = '500 Internal Server Error'
        response_body = f"An error occurred: {e}".encode('utf-8')

    # The headers list is now empty or minimal, to be handled by Nginx
    headers = [] 
    start_response(status, headers)
    return [response_body]