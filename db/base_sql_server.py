import pymssql
import datetime

class BaseSQLServer:

	def __init__(self, config):
		try:
			self.conf = config
			self.server = self.conf['server']
			self.user = self.conf['user']
			self.password = self.conf['password']
			self.database = self.conf['database']
			self.conn = pymssql.connect(self.server, self.user, self.password, self.database)
			self.cursor = self.conn.cursor()
		except Exception as e:
			print("Error: {}".format(e))

	def get_connect(self, ):
		self.conn = pymssql.connect(self.server, self.user, self.password, self.database)
		self.cursor = self.conn.cursor()

	def query(self, query, json=True):
		try:
			self.conn = pymssql.connect(self.server, self.user, self.password, self.database)
			self.cursor = self.conn.cursor()
			self.cursor.execute(query)
			rows = self.cursor.fetchall()
			self.conn.close()
			if json:
				return [dict(
					(self.cursor.description[i][0],
						value.isoformat() if isinstance(value, datetime.datetime) else value)
					for i, value in enumerate(row)) for row in rows]
			return rows
		except Exception as e:
			print(query)
			print("Error: {}".format(e))
			return []

	def execute(self, query):
		try:
			self.conn = pymssql.connect(self.server, self.user, self.password, self.database)
			self.cursor = self.conn.cursor()
			self.cursor.execute(query)
			self.conn.commit()
			self.conn.close()
			return True
		except Exception as e:
			print("Error: {}".format(e))
			return False

