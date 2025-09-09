import json
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class VehicleRegistrationCertificate:
    def __init__(self, data: dict):
        self.nombre_de_la_empresa = data.get("nombre_de_la_empresa")
        self.fecha_de_emision = data.get("fecha_de_emision")
        self.serie_de_numero_de_factura_1 = data.get("serie_de_numero_de_factura_1")
        self.numero_de_factura_1 = data.get("numero_de_factura_1")
        self.fecha_de_factura_1 = data.get("fecha_de_factura_1")
        self.placa = data.get("placa")
        self.marca = data.get("marca")
        self.modelo = data.get("modelo")
        self.ano_de_fabricacion = data.get("ano_de_fabricacion")
        self.serial_niv = data.get("serial_niv")
        self.ano_modelo = data.get("ano_modelo")
        self.serial_chasis = data.get("serial_chasis")
        self.serial_motor = data.get("serial_motor")
        self.serial_carrocería = data.get("serial_carrocería")
        self.serial_carrocería = data.get("serial_carrocería")
        self.clase = data.get("clase")
        self.tipo = data.get("tipo")
        self.uso = data.get("uso")
        self.servicio = data.get("servicio")
        self.color_pr = data.get("color_pr")
        self.color_sec = data.get("color_sec")
        self.n_puestos = data.get("n_puestos")
        self.n_ejes = data.get("n_ejes")
        self.peso_tara = data.get("peso_tara")
        self.cap_de_carga = data.get("cap_de_carga")
        self.puerto_de_entrada = data.get("puerto_de_entrada")
        self.planilla_liq_grv_n = data.get("planilla_liq_grv_n")
        self.planilla_liq_grv_fecha = data.get("planilla_liq_grv_fecha")
        self.factura_de_adquisicion_n = data.get("factura_de_adquisicion_n")
        self.factura_de_adquisicion_fecha = data.get("factura_de_adquisicion_fecha")
        self.refeciv = data.get("refeciv")
        self.homologacion_n = data.get("homologacion_n")
        self.homologacion_fecha = data.get("homologacion_fecha")
        self.fecha_fin_convenio = data.get("fecha_fin_convenio")
                
        self.fields = list(vars(self).items())

def generate_sniper_pdf(decoded_body: str) -> bytes:
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)

    page_width, page_height = letter
    wu = page_width / 100
    hu = page_height / 100
    
    data = json.loads(decoded_body)    
    content = VehicleRegistrationCertificate(data)
    
    c.drawString(wu*23, hu*84, content.nombre_de_la_empresa)    
    c.drawString(wu*69, hu*71, content.uso)

    c.save()
    buffer.seek(0)
    return buffer.getvalue()