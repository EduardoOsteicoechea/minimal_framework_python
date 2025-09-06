import os
from generate_sniper_pdf import generate_sniper_pdf

STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')


def application(environ, start_response):
    path = environ.get('PATH_INFO', '')

    if path == '/api/sniper':
        if environ['REQUEST_METHOD'] == 'OPTIONS':
            status = '200 OK'
            start_response(status, [])
            return [b'']

        if environ['REQUEST_METHOD'] == 'POST':
            try:
                content_length = int(environ.get('CONTENT_LENGTH', 0))
                request_body = environ['wsgi.input'].read(content_length)
                decoded_body = request_body.decode('utf-8')
                pdf_data = generate_sniper_pdf(decoded_body)

                status = '200 OK'
                headers = [
                    ('Content-type', 'application/pdf'),
                    ('Content-Disposition', 'attachment; filename="report.pdf"'),
                    ('Content-Length', str(len(pdf_data)))
                ]
                start_response(status, headers)
                return [pdf_data]
            except Exception as e:
                status = '500 Internal Server Error'
                error_headers = [('Content-type', 'text/plain')]
                start_response(status, error_headers)
                error_message = f"An error occurred while processing POST request: {e}"
                return [error_message.encode('utf-8')]
        else:
            status = '200 OK'
            headers = [('Content-type', 'text/html')]
            start_response(status, headers)
            response_body = "This endpoint is ready to receive a POST request."
            return [response_body.encode('utf-8')]

    if path == '/api/':
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

    start_response('404 Not Found', [('Content-type', 'text/plain')])
    return [b'Path not found']
