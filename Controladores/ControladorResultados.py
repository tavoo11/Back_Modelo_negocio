from Repositorios.RepositorioResultados import RepositorioResultados
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Resultados import Resultados
from Modelos.Candidato import Candidato
from Modelos.Mesa import Mesa


class ControladorResultados():
    def __init__(self):
        self.repositorioResultados = RepositorioResultados()
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioMesa = RepositorioMesa()

    def index(self):
        return self.repositorioResultados.findAll()

    def create(self, infoResultados, id_candidato, id_mesa):
        nuevaResultado = Resultados(infoResultados)
        candidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        mesa = Mesa(self.repositorioMesa.findById(id_mesa))
        nuevaResultado.candidato = candidato
        nuevaResultado.mesa = mesa
        return self.repositorioResultados.save(nuevaResultado)

    def show(self, id):
        laResultado = RepositorioResultados.findById(id)
        return laResultado.__dict__

    def update(self, id, elResultado, id_candidato, id_mesa):
        resultadoActual = RepositorioResultados.findById(id)
        resultadoActual.cantidadVotos = elResultado["cantidadVotos"]
        candidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        mesa = Mesa(self.repositorioMesa.findById(id_mesa))
        resultadoActual.candidato = candidato
        resultadoActual.mesa = mesa
        return self.repositorioResultados.save(resultadoActual)

    def delete(self, id):
        return self.repositorioResultados.delete(id)
