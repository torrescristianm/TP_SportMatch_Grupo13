class Equipo:
    def __init__(self, nombre, pais, liga, fundacion, popularidad, titulos, estilo):
        self.nombre = nombre
        self.pais = pais
        self.liga = liga
        self.fundacion = fundacion
        self.popularidad = popularidad
        self.titulos = titulos
        self.estilo = estilo

    def coincide_con_nombre(self, texto):
        return texto.lower() in self.nombre.lower()

    def __str__(self):
        return (
            f"{self.nombre} | {self.pais} | {self.liga} | "
            f"popularidad: {self.popularidad} | titulos: {self.titulos}"
        )
