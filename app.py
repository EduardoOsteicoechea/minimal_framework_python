import os
from base_page import BasePage
from generate_sniper_pdf import generate_sniper_pdf

STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')
    
api_route =  "/api"
data_files_route =  "data_file/"

generate_printing =  {
    "api_url":f"{api_route}/certispot/generar/impresion",
    "page_url":"/certispot/generar/impresion",
    "page_title":"Impresión Perfecta para tus Certificados",
    "ui_generator":"/certispot/generar/regristros",
    "data_file":f"{data_files_route}sniper_base.json"
}

generate_registries = {
    "api_url":f"{api_route}/certispot/generar/regristros",
    "page_url":"/certispot/generar/regristros",
    "page_title":"Genera Registros para importación de vehículos para el INTT",
    "ui_generator":"/certispot/generar/regristros",
    "data_file":"f{data_files_route}sniper_base.json"
}
    
def application(environ, start_response):
    path = environ.get('PATH_INFO', '/')
    status = '200 OK'
    response_body = b'Path not found'
    try:
        if path == api_route:
            response_body = b"Working"
        
        elif path == '/':
            page = BasePage("Eduardo Osteicoechea")
            response_body = page.html().encode('utf-8')
            
        elif path == generate_printing["api_url"]:
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
            
        elif path == '/article':
            page = BasePage("Artículos", ["article"], ["article"], True, "data_file/un_dios_prudente.json")
            response_body = page.html().encode('utf-8')
            
        elif path == '/songs':
            page = BasePage("Cánticos", ["article", "songs"], ["songs"], True, "data_file/orquesta_del_desierto.json")
            response_body = page.html().encode('utf-8')
            
        elif path == generate_printing["page_url"]:
            page = BasePage(
                generate_printing["page_title"], 
                ["sniper_base"], 
                ["sniper_base"],
                False,
                generate_printing["data_file"],
                generate_printing["api_url"]
            )
            response_body = page.html().encode('utf-8')
            
        elif path == generate_registries["page_url"]:
            page = BasePage(
                generate_registries["page_title"], 
                ["sniper_base"], 
                ["sniper_base"], 
                False,  
                generate_registries["data_file"],
                generate_registries["api_url"]
            )
            response_body = page.html().encode('utf-8')
        
        else:
            status = '404 Not Found'
            response_body = b'Path not found'
            
    except Exception as e:
        status = '500 Internal Server Error'
        response_body = f"An error occurred: {e}".encode('utf-8')

    # The headers list is empty, to be handled by Nginx
    headers = [] 
    start_response(status, headers)
    return [response_body]