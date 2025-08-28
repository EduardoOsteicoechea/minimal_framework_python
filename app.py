# app.py

def application(environ, start_response):
    """
    A bare-bones WSGI application.
    """
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]

    start_response(status, headers)

    # The body of the response, returned as an iterable of byte strings.
    response_body = "Change from local. Thanks lord. Check"
    
    return [response_body.encode('utf-8')]