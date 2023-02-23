from Repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Mesa import Mesa


class ControladorMesa():
    def __init__(self):
        self.repositorioMesa = RepositorioMesa()

    def index(self):
        return self.repositorioMesa.findAll()

    def create(self, infoMesa):
        nuevaMesa = Mesa(infoMesa)
        return self.repositorioMesa.save(nuevaMesa)

    def show(self, id):
        laMesa = RepositorioMesa.findById(id)
        return laMesa.__dict__

    def update(self, id, laMesa):
        mesaActual = Mesa(self.repositorioMesa.findById(id))
        mesaActual.numero = laMesa["numero"]
        mesaActual.cantidadInscritos = laMesa["cantidadInscritos"]
        return self.repositorioMesa.save(mesaActual)

    def delete(self, id):
        return self.repositorioMesa.delete(id)
