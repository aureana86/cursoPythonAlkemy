from enum import Enum


class TipoInstrumento(Enum):
    PERC = "Percusion"
    VTO = "Viento"
    CUER = "Cuerda"


class Instrumento:
    def __init__(self, id, precio, tipoInstrumento):
        self.id = id
        self.precio = precio
        self.tipoInstrumento = tipoInstrumento


class Sucursal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.instrumentos = []

    def listarInstrumentos(self):
        for instrumento in self.instrumentos:
            print(f"ID: {instrumento.id}, Precio: {instrumento.precio},"
                  f" Tipo: {instrumento.tipoInstrumento.name}")

    def instrumentosPorTipo(self, tipo):
        return [instrumento for instrumento in self.instrumentos
                if instrumento.tipoInstrumento == tipo]


class Fabrica:
    def __init__(self):
        self.listaSucursales = []

    def listarInstrumentos(self):
        for sucursal in self.listaSucursales:
            print(f"\nSucursal: {sucursal.nombre}")
            sucursal.listarInstrumentos()

    def instrumentosPorTipo(self, tipo):
        instrumentos_filtrados = []
        for sucursal in self.listaSucursales:
            instrumentos_filtrados.extend(sucursal.instrumentosPorTipo(tipo))
        return instrumentos_filtrados


if __name__ == "__main__":

    suc1 = Sucursal("Sucursal A")
    suc1.instrumentos.append(Instrumento("SA001", 500, TipoInstrumento.PERC))
    suc1.instrumentos.append(Instrumento("SA002", 700, TipoInstrumento.VTO))

    suc2 = Sucursal("Sucursal B")
    suc2.instrumentos.append(Instrumento("SB003", 300, TipoInstrumento.CUER))
    suc2.instrumentos.append(Instrumento("SB004", 900, TipoInstrumento.PERC))

    suc3 = Sucursal("Sucursal C")
    suc3.instrumentos.append(Instrumento("SC005", 200, TipoInstrumento.CUER))
    suc3.instrumentos.append(Instrumento("SC006", 100, TipoInstrumento.VTO))

    suc4 = Sucursal("Sucursal D")
    suc4.instrumentos.append(Instrumento("SD03", 400, TipoInstrumento.CUER))
    suc4.instrumentos.append(Instrumento("SD004", 250, TipoInstrumento.PERC))

    fabrica = Fabrica()
    fabrica.listaSucursales.extend([suc1, suc2, suc3, suc4])

    # A) Listar instrumentos
    fabrica.listarInstrumentos()

    # B) Instrumentos por tipo
    tipo_deseado = TipoInstrumento.CUER
    instrumentos_filtrados = fabrica.instrumentosPorTipo(tipo_deseado)
    print(f"\nInstrumentos de tipo {tipo_deseado.name}:")
    for instrumento in instrumentos_filtrados:
        print(f"ID: {instrumento.id}, Precio: {instrumento.precio},"
              f" Tipo: {instrumento.tipoInstrumento.name}")
