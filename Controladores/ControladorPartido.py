from Repositorios.RepositorioPartido import RespositorioPartido
from Modelos.Partido import Partido


class ControladorPartido:
    def __init__(self):
        self.repositorioPartido = RespositorioPartido()

    def index(self):
        return self.repositorioPartido.findAll()

    def create(self, infoPartido):
        nuevoPartido = Partido(infoPartido)
        return self.repositorioPartido.save(nuevoPartido)

    def show(self, id):
        elPartido = Partido(RespositorioPartido.findById(id))
        return elPartido.__dict__

    def update(self, id, infoPartido):
        partidoActual = Partido(RespositorioPartido.findById(id))
        partidoActual.nombre = infoPartido["nombre"]
        partidoActual.lema = infoPartido["lema"]
        return self.repositorioPartido.save(partidoActual)

    def delete(self, id):
        return self.repositorioPartido.delete(id)
