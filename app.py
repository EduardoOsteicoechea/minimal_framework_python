# app.py

from pages.home import HomePage


def application(environ, start_response):
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
