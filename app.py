# app.py

from pages import home

def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    
    page_instance = home.Page()
    # page_instance = page.Page()
    # page_instance.set_title("My Python-Generated Page")
    # page_instance.add_css(["main_styles"])
    # page_instance.set_content_block("main_content", "<h1>Welcome!</h1><p>This page was created with Python.</p>")
    # page_instance.add_js_bottom(["main_script"], is_module=True)

    response_body = page_instance.html()
        
    return [response_body.encode('utf-8')]