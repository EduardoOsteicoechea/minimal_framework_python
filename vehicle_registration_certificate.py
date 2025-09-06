class VehicleRegistrationCertificate:

    def __init__(self, data: dict):
        self.nombre_de_la_empresa = data.get("nombre_de_la_empresa")
        self.fecha_emision = data.get("fecha_emision")
        self.factura_1_n_fecha = data.get("factura_1_n_fecha")
        self.fields = [
            ["nombre_de_la_empresa", self.nombre_de_la_empresa],
            ["fecha_emision", self.fecha_emision],
            ["factura_1_n_fecha", self.factura_1_n_fecha],
        ]
