import os
from generate_sniper_pdf import generate_sniper_pdf

STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')

def application(environ, start_response):
    path = environ.get('PATH_INFO', '')
    status = '200 OK'

    if path == '/api/sniper':
        status = '200 OK'
        headers = [
            ('Access-Control-Allow-Origin', '*'),
            ('Access-Control-Allow-Methods', 'GET, POST, OPTIONS'),
            ('Access-Control-Allow-Headers', 'Content-Type')
        ]
        if environ['REQUEST_METHOD'] == 'POST':
            try:
                content_length = int(environ.get('CONTENT_LENGTH', 0))
                request_body = environ['wsgi.input'].read(content_length)
                decoded_body = request_body.decode('utf-8')
                pdf_data = generate_sniper_pdf(decoded_body)
                headers.append(('Content-type', 'application/pdf'))
                headers.append(('Content-Disposition', 'attachment; filename="report.pdf"'))
                headers.append(('Content-Length', str(len(pdf_data))))
                start_response(status, headers)
                return [pdf_data]
            except Exception as e:
                status = '500 Internal Server Error'
                error_headers = [('Content-type', 'text/plain')]
                start_response(status, error_headers)
                error_message = f"An error occurred while processing POST request: {e}"
                return [error_message.encode('utf-8')]                
        else:
            headers.append(('Content-type', 'text/html'))
            start_response(status, headers)
            response_body = "This endpoint is ready to receive a POST request."
            return [response_body.encode('utf-8')]

    if path.startswith('/static/'):
        filename = path.replace('/static/', '')
        filepath = os.path.join(STATIC_DIR, filename)

        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                content = f.read()
            if filename.endswith('.css'):
                content_type = 'text/css'
            elif filename.endswith('.js'):
                content_type = 'application/javascript'
            elif filename.endswith('.ico'):
                content_type = 'image/x-icon'
            elif filename.endswith('.png'):
                content_type = 'image/png'
            elif filename.endswith('.jpg'):
                content_type = 'image/jpeg'
            else:
                content_type = 'application/octet-stream'
            headers = [('Content-type', content_type),
                       ('Content-Length', str(len(content)))]
            start_response('200 OK', headers)
            return [content]
        else:
            start_response('404 Not Found', [('Content-type', 'text/plain')])
            return [b'File not found']

    if path == '/':
        status = '200 OK'
        headers = [('Content-type', 'text/html')]
        start_response(status, headers)
        try:
            response_body = "Working"
            return [response_body.encode('utf-8')]
        except Exception as e:
            status = '500 Internal Server Error'
            headers = [('Content-type', 'text/plain')]
            start_response(status, headers)
            error_message = f"An error occurred: {e}"
            return [error_message.encode('utf-8')]
        

    # start_response('404 Not Found', [('Content-type', 'text/plain')])
    # return [b'Path not found']
