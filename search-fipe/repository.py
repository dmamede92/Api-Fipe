from datetime import date
from connection import Conexao
from decimal import Decimal


class BotRepository:
	def save(self, ano_modelo, valor, codigoFipe):
		connection = Conexao()
		cursor = connection.cursor
		data_atual = date.today()
		sql = ("INSERT INTO tb_processamento_bot VALUES ('" + str(codigoFipe) + "', '" + str(ano_modelo)  + "', '" + str(valor.replace(',','.').replace('R$', '').replace(" ", "")) + "', '" + str(data_atual) +"' )")
		
		cursor.execute(sql)
		connection.con.commit()
		cursor.close
		
		print("Processamento: " + str(codigoFipe) + " salvo com sucesso!")


	