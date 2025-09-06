import json
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class VehicleRegistrationCertificate:
    def __init__(self, data: dict):
        self.nombre_de_la_empresa = data.get("nombre_de_la_empresa")
        self.fecha_emision = data.get("fecha_emision")
        self.factura_1_n_fecha = data.get("factura_1_n_fecha")
        self.placa = data.get("placa")
        self.marca = data.get("marca")
        self.modelos = data.get("modelos")
        self.ano_de_fabricacion = data.get("ano_de_fabricacion")
        
        self.fields = list(vars(self).items())

        # self.fields = [
        #     ["nombre_de_la_empresa", self.nombre_de_la_empresa],
        #     ["fecha_emision", self.fecha_emision],
        #     ["factura_1_n_fecha", self.factura_1_n_fecha],
        # ]

def generate_sniper_pdf(decoded_body: str) -> bytes:
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    
    data = json.loads(decoded_body)
    content = VehicleRegistrationCertificate(data)

    vertical_location_counter = 700 # Start from the top of the page
    for field_name, value in content.fields:
        line = f"{field_name.replace('_', ' ').title()}: {value}"
        c.drawString(72, vertical_location_counter, line) # 72 is 1 inch
        vertical_location_counter -= 15 # Move down for the next line

    c.save()
    buffer.seek(0)
    return buffer.getvalue()