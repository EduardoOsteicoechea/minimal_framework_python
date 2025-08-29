# app.py

from pages import home

def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)

    try:
    # page_instance = page.Page()
    # page_instance.set_title("My Python-Generated Page")
    # page_instance.add_css(["main_styles"])
    # page_instance.set_content_block("main_content", "<h1>Welcome!</h1><p>This page was created with Python.</p>")
    # page_instance.add_js_bottom(["main_script"], is_module=True)
      page_instance = home.Page()
      response_body = page_instance.html()
      return [response_body.encode('utf-8')]
    except Exception as e:
        # Return a concise exception message for clarity.
        return f"An error occurred: {e}"
