import json
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class VehicleRegistrationCertificate:
    def __init__(self, data: dict):
        self.nombre_de_la_empresa = [235, 834.5, data.get("nombre_de_la_empresa")]
        
        self.fecha_de_emision = [188, 813, data.get("fecha_de_emision")]
        self.serie_de_numero_de_factura_1 = [513, 813, data.get("serie_de_numero_de_factura_1")]
        self.numero_de_factura_1 = data.get("numero_de_factura_1")
        self.fecha_de_factura_1 = data.get("fecha_de_factura_1")
        
        self.placa = [134, 793, data.get("placa")]        
        self.marca = [299, 793, data.get("marca")]        
        self.modelo = [677, 793, data.get("modelo")]
        
        self.ano_de_fabricacion = [217, 772, data.get("ano_de_fabricacion")]
        self.serial_niv = data.get("serial_niv")
        self.ano_modelo = data.get("ano_modelo")
        self.serial_chasis = data.get("serial_chasis")
        self.serial_motor = data.get("serial_motor")
        self.serial_carrocería = data.get("serial_carrocería")
        self.serial_carrocería = data.get("serial_carrocería")
        self.clase = data.get("clase")
        self.tipo = data.get("tipo")
        self.uso = [695, 713, data.get("uso")]
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
    wu = page_width / 1000
    hu = page_height / 1000
    
    data = json.loads(decoded_body)    
    content = VehicleRegistrationCertificate(data)
    
    c.drawString(wu * content.nombre_de_la_empresa[0], hu * content.nombre_de_la_empresa[1], content.nombre_de_la_empresa[2])
    c.drawString(wu * content.fecha_de_emision[0], hu * content.fecha_de_emision[1], content.fecha_de_emision[2])
    c.drawString(wu * content.serie_de_numero_de_factura_1[0], hu * content.serie_de_numero_de_factura_1[1], content.serie_de_numero_de_factura_1[2] + " " + content.numero_de_factura_1 + " / " + content.fecha_de_factura_1[0:4] + "-" + content.fecha_de_factura_1[4:6] + "-" + content.fecha_de_factura_1[6:8])
        
    c.drawString(wu * content.placa[0], hu * content.placa[1], content.placa[2])
    c.drawString(wu * content.marca[0], hu * content.marca[1], content.marca[2])
    c.drawString(wu * content.modelo[0], hu * content.modelo[1], content.modelo[2])
    
    c.drawString(wu * content.uso[0], hu * content.uso[1], content.uso[2])

    c.save()
    buffer.seek(0)
    return buffer.getvalue()