import psycopg2

class Conexao:
	def __init__(self):
		self.conn_string = """
					host='192.168.254.141'
					dbname='db_frota'
					user='postgres'
					password='123'
					port='5433' 
					"""
		try:
			
			self.con = psycopg2.connect(self.conn_string)	
			self.cursor = self.con.cursor()		

		except psycopg2.Error as e:
			returnprint('Falha na conexao!\n')