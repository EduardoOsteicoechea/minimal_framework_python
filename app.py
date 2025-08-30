import os
from pages.home import HomePage

STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')

def application(environ, start_response):
    path = environ.get('PATH_INFO', '')

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
            page_instance = HomePage()
            response_body = page_instance.html()
            return [response_body.encode('utf-8')]
        except Exception as e:
            status = '500 Internal Server Error'
            headers = [('Content-type', 'text/plain')]
            start_response(status, headers)
            error_message = f"An error occurred: {e}"
            return [error_message.encode('utf-8')]
    
    start_response('404 Not Found', [('Content-type', 'text/plain')])
    return [b'Path not found']