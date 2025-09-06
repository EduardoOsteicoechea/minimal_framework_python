class VehicleRegistrationCertificate:
    def __init__(self, data):
        # 1
        self.nombre_de_la_empresa = data.nombre_de_la_empresa
        # 2
        self.fecha_emision = data.fecha_emision
        # 3
        self.factura_1_n_fecha = data.factura_1_n_fecha

        self.fields = [
            ["nombre_de_la_empresa", self.nombre_de_la_empresa],
            ["fecha_emision", self.fecha_emision],
            ["factura_1_n_fecha", self.factura_1_n_fecha],
        ]

    def print(self):
        output_lines = []
        for field_name, value in self.fields:
            output_lines.append(f"{field_name}: {value}")
        return "\n".join(output_lines)
