from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

from vehicle_registration_certificate import VehicleRegistrationCertificate

def generate_sniper_pdf(decoded_body: str) -> bytes:
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    content = VehicleRegistrationCertificate(decoded_body)
    
    vertical_location_counter = 5
    for field in content.print():
        c.drawString(5, vertical_location_counter, field)
        vertical_location_counter += 5
    x_pos_inches = 2 * inch
    y_pos_inches = 3 * inch
    page_height = letter[1]
    # c.drawString(x_pos_inches, page_height - y_pos_inches, "Text placed using inches.")
    c.save()
    buffer.seek(0)
    return buffer.getvalue()