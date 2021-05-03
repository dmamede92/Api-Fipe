from datetime import date
import requests 
import json
import time
from repository import BotRepository


class ApiController:
	def process(self):
		url_base = "http://fipeapi.appspot.com/api/1/carros/marcas.json"
		requestMarcas = requests.get(url_base)
		print(requestMarcasf)
		for marca in requestMarcas:
			time.sleep(5)
			self.processaMarca(marca['id'])


	def register(self, cd_fipe):
		repository = BotRepository()
		url_base = "http://fipeapi.appspot.com/api/1/carros/veiculo/0/" + str(cd_fipe)
		request = requests.get(url_base + ".json").json()
		print("olha os modelos: " + str(request) +"\n")

		for i in request:
			response = requests.get(url_base + "/" + str(i['id']) + ".json").json()
			preco = response['preco']
			repository.save(str(response['ano_modelo']), preco, cd_fipe)
			

	def processaMarca(self, idMarca):
		url_modelos = "http://fipeapi.appspot.com/api/1/carros/veiculos/" + str(idMarca)
		requestVeiculos = requests.get(url_modelos + ".json").json()

		for veiculo in requestVeiculos:
			time.sleep(4)
			self.processaVeiculo(veiculo['id'], idMarca)


	def processaVeiculo(self, idVeiculo, idMarca):
		url_veiculos = "http://fipeapi.appspot.com/api/1/carros/veiculo/" + str(idMarca) + "/" + str(idVeiculo)
		requestModelos = requests.get(url_veiculos + ".json")

		print(requestModelos)
		for modelo in requestModelos:
			print(modelo)
			time.sleep(5)
			self.processaCodigoFipe(modelo['id'], url_veiculos)
			break


	def processaCodigoFipe(self, idModelo, url_base):
		requestFipe = requests.get(url_base + "/" + str(idModelo) + ".json").json()		
		codigoFipe = requestFipe['fipe_codigo']
		
		self.register(codigoFipe)
