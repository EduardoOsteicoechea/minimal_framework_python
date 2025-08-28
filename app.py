# app.py

def application(environ, start_response):
    """
    A bare-bones WSGI application.
    """
    status = '200 OK'
    headers = [('Content-type', 'text/html')]

    start_response(status, headers)

    response_body = """

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="static/style.css">
  <title>Document</title>
</head>
<body>
    Change from local. Thanks lord. Check aaaaaaaaaaaaaaaaaaaaa
</body>

"""
    
    return [response_body.encode('utf-8')]