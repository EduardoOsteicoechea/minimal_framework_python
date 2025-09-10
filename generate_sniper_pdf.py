import json
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

class VehicleRegistrationCertificate:
    def __init__(self, data: dict):
        self.nombre_de_la_empresa = [235, 834, data.get("nombre_de_la_empresa")]
        
        x1 = 217
        x2 = 300
        x3 = 535
        x4 = 777  
        y = 836
        y_reduction = 20
        
        y -= y_reduction        
        self.fecha_de_emision = [x1, y, data.get("fecha_de_emision")]
        self.serie_de_numero_de_factura_1 = [x3, y, data.get("serie_de_numero_de_factura_1")]
        self.numero_de_factura_1 = data.get("numero_de_factura_1")
        self.fecha_de_factura_1 = data.get("fecha_de_factura_1")
        
        y -= y_reduction
        self.placa = [134, y, data.get("placa")]        
        self.marca = [x2, y, data.get("marca")]        
        self.modelo = [x4, y, data.get("modelo")]
        
        y -= y_reduction
        self.ano_de_fabricacion = [x1, y, data.get("ano_de_fabricacion")]
        self.serial_niv = [x3, y, data.get("serial_niv")]
        
        y -= y_reduction
        self.ano_modelo = [x1, y, data.get("ano_modelo")]
        self.serial_chasis = [x3, y, data.get("serial_chasis")]
        
        y -= y_reduction
        self.serial_motor = [x1, y, data.get("serial_motor")]
        self.serial_carrocería = [x3, y, data.get("serial_carrocería")]
        
        y -= y_reduction
        self.clase = [x1, y, data.get("clase")]
        self.tipo = [430, y, data.get("tipo")]
        self.uso = [x4, y, data.get("uso")]
        
        y -= y_reduction
        self.servicio = [x1, y, data.get("servicio")]
        self.color_pr = [x3, y, data.get("color_pr")]
        self.color_sec = [x4, y, data.get("color_sec")]
        
        y -= y_reduction
        self.n_puestos = [x1, y, data.get("n_puestos")]
        self.n_ejes = [370, y, data.get("n_ejes")]
        self.peso_tara = [x3, y, data.get("peso_tara")]
        self.cap_de_carga = [x4, y, data.get("cap_de_carga")]
        
        y -= y_reduction
        self.puerto_de_entrada = [x1, y, data.get("puerto_de_entrada")]        
        self.planilla_liq_grv_n = [587, y, data.get("planilla_liq_grv_n")]
        self.planilla_liq_grv_fecha = data.get("planilla_liq_grv_fecha")
        
        y -= y_reduction
        self.factura_de_adquisicion_n = [x2, y, data.get("factura_de_adquisicion_n")]
        self.factura_de_adquisicion_fecha = data.get("factura_de_adquisicion_fecha")
        self.refeciv = [x4, y, data.get("refeciv")]       
        
        y -= y_reduction
        self.homologacion_n = [x2, y, data.get("homologacion_n")]
        self.homologacion_fecha = data.get("homologacion_fecha")
        self.fecha_fin_convenio = [x4, y, data.get("fecha_fin_convenio")]
                
        self.fields = list(vars(self).items())
        
HIGH_RES_LETTER = (8.5 * inch * 4.1666, 11 * inch * 4.1666) # Scales 72 DPI to 300 DPI (300/72=4.1666)

def generate_sniper_pdf(decoded_body: str) -> bytes:
    buffer = BytesIO()
    # c = canvas.Canvas(buffer, pagesize=HIGH_RES_LETTER)
    c = canvas.Canvas(buffer, pagesize=letter)
    c.setFont("Helvetica-Bold", 8)

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
    
    c.drawString(wu * content.ano_de_fabricacion[0], hu * content.ano_de_fabricacion[1], content.ano_de_fabricacion[2])
    c.drawString(wu * content.serial_niv[0], hu * content.serial_niv[1], content.serial_niv[2])

    c.drawString(wu * content.ano_modelo[0], hu * content.ano_modelo[1], content.ano_modelo[2])
    c.drawString(wu * content.serial_chasis[0], hu * content.serial_chasis[1], content.serial_chasis[2])

    c.drawString(wu * content.serial_motor[0], hu * content.serial_motor[1], content.serial_motor[2])
    c.drawString(wu * content.serial_carrocería[0], hu * content.serial_carrocería[1], content.serial_carrocería[2])
    
    c.drawString(wu * content.clase[0], hu * content.clase[1], content.clase[2])
    c.drawString(wu * content.tipo[0], hu * content.tipo[1], content.tipo[2])
    c.drawString(wu * content.uso[0], hu * content.uso[1], content.uso[2])

    c.drawString(wu * content.servicio[0], hu * content.servicio[1], content.servicio[2])
    c.drawString(wu * content.color_pr[0], hu * content.color_pr[1], content.color_pr[2])
    c.drawString(wu * content.color_sec[0], hu * content.color_sec[1], content.color_sec[2])

    c.drawString(wu * content.n_puestos[0], hu * content.n_puestos[1], content.n_puestos[2])
    c.drawString(wu * content.n_ejes[0], hu * content.n_ejes[1], content.n_ejes[2])
    c.drawString(wu * content.peso_tara[0], hu * content.peso_tara[1], content.peso_tara[2])
    c.drawString(wu * content.cap_de_carga[0], hu * content.cap_de_carga[1], content.cap_de_carga[2])

    c.drawString(wu * content.puerto_de_entrada[0], hu * content.puerto_de_entrada[1], content.puerto_de_entrada[2])
    c.drawString(wu * content.planilla_liq_grv_n[0], hu * content.planilla_liq_grv_n[1], content.planilla_liq_grv_n[2] +  " " + content.planilla_liq_grv_fecha)

    c.drawString(wu * content.factura_de_adquisicion_n[0], hu * content.factura_de_adquisicion_n[1], content.factura_de_adquisicion_n[2] + " " + content.factura_de_adquisicion_fecha)
    c.drawString(wu * content.refeciv[0], hu * content.refeciv[1], content.refeciv[2])
    
    c.drawString(wu * content.homologacion_n[0], hu * content.homologacion_n[1], content.homologacion_n[2] + " " + content.homologacion_fecha)
    c.drawString(wu * content.fecha_fin_convenio[0], hu * content.fecha_fin_convenio[1], content.fecha_fin_convenio[2])


    c.save()
    buffer.seek(0)
    return buffer.getvalue()