from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import pymongo
import certifi
from pymongo.server_api import ServerApi

ca = certifi.where()

client = pymongo.MongoClient(
    "mongodb+srv://elecciones:elecciones@cluster0.abqd073.mongodb.net/?retryWrites=true&w=majority",
    server_api=ServerApi('1'))
db = client.test

print(db)
baseDatos = client["baseVotaciones"]
print(baseDatos.list_collection_names())
app = Flask(__name__)
cors = CORS(app)

from Controladores.ControladorCandidato import ControladorCandidato

controladorCandidato = ControladorCandidato()


@app.route("/candidato/<string:id>/partido/<string:id_partido>", methods=['PUT'])
def asignarPartidoAcandidato(id, id_partido):
    json = controladorCandidato.asignarPartido(id, id_partido)
    return jsonify(json)


@app.route("/candidato", methods=['GET'])
def obtenerCandidato():
    json = controladorCandidato.index()
    return jsonify(json)


@app.route("/candidato", methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json = controladorCandidato.create(data)
    return jsonify(json)


@app.route("/candidato/<string:id>", methods=['GET'])
def obtenCandidatoId(id):
    json = controladorCandidato.show(id)
    return jsonify(json)


@app.route("/candidato/<string:id>", methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json = controladorCandidato.update(id, data)
    return jsonify(json)


@app.route("/candidato/<string:id>", methods=['DELETE'])
def eliminarCandidato(id):
    json = controladorCandidato.delete(id)
    return jsonify(json)


from Controladores.ControladorPartido import ControladorPartido

controladorPartido = ControladorPartido()


@app.route("/partidos", methods=['GET'])
def obtenerPartido():
    json = controladorPartido.index()
    return jsonify(json)


@app.route("/partidos", methods=['POST'])
def crearPartido():
    data = request.get_json()
    json = controladorPartido.create(data)
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=['GET'])
def obtenPartidoId(id):
    json = controladorPartido.show(id)
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json = controladorPartido.update(id, data)
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=['DELETE'])
def eliminarPartido(id):
    json = controladorPartido.delete(id)
    return jsonify(json)


from Controladores.ControladorMesa import ControladorMesa

controladorMesa = ControladorMesa()


@app.route("/mesa", methods=['GET'])
def obtenerMesa():
    json = controladorMesa.index()
    return jsonify(json)


@app.route("/mesa", methods=['POST'])
def crearMesa():
    data = request.get_json()
    json = controladorMesa.create(data)
    return jsonify(json)


@app.route("/mesa/<string:id>", methods=['GET'])
def obtenMesaId(id):
    json = controladorMesa.show(id)
    return jsonify(json)


@app.route("/mesa/<string:id>", methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json = controladorMesa.update(id, data)
    return jsonify(json)


@app.route("/mesa/<string:id>", methods=['DELETE'])
def eliminarMesa(id):
    json = controladorMesa.delete(id)
    return jsonify(json)


from Controladores.ControladorResultados import ControladorResultados

controladorResultados = ControladorResultados()


@app.route("/resultados", methods=['GET'])
def obtenerResultados():
    json = controladorResultados.index()
    return jsonify(json)


@app.route("/resultados/candidato/<string:id_candidato>/mesa/<string:id_mesa>", methods=['POST'])
def crearResultados(id_candidato, id_mesa):
    data = request.get_json()
    json = controladorResultados.create(data, id_candidato, id_mesa)
    return jsonify(json)


@app.route("/resultados/<string:id>", methods=['GET'])
def obtenResultadosId(id):
    json = controladorResultados.show(id)
    return jsonify(json)


@app.route("/resultados/<string:id>/candidato/<string:id_candidato>/mesa/<string:id_mesa>", methods=['PUT'])
def modificarResultados(id, id_candidato, id_mesa):
    data = request.get_json()
    json = controladorResultados.update(id, data, id_candidato, id_mesa)
    return jsonify(json)


@app.route("/resultados/<string:id>", methods=['DELETE'])
def eliminarResultados(id):
    json = controladorResultados.delete(id)
    return jsonify(json)


@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
