#coding:utf-8
#coding by N30-Geek
#=====================================
#
# Ce script principale du code
# ici il y a presque tout ce qui comporte les jeux

#=====================================

# importation des modules utiliser dans code princapale


import os, time
import sqlite3 as sql
import hashlib 

# La classe principale de gestion d'utilisateur
class Users:
	"""
		La class users:
		LES METHODES DE CETTE CLASSE:
		** userRegister
		** connectionUser

		*Description:
		 ------------
		
		Cette classe permet de connecter l'utilisateur

	"""
	def __init__(self):

		self.conn = createDataBase()
		self.user_name = user_name
		self.con = self.connection[0]
		self.cur = self.con.cursor()

	def userRegister(self, user_name, user_pass):
		"""
			Cette méthode permet d'enregistrer un nouveau utilisateur
			de jeux.

			Retourne 'ok' si tout se passe bien
		"""
		self.user_pass = user_pass
		self.user_data = {
			self.user_name,
			self.user_pass
		}

		try:
			self.cur.execute("""
				INSERT INTO users (
					u_name,
					u_password
				) VALUES (
					?, ?
				)
			""", self.user_data)

			self.con.commit()
			self.con.close()

		except Exception as e:
			return "Les donnee ne pas enregistrer dans la base de donnnée \n Il peut qu'il y a un probleme"
		else:
			return "Donnee enregistrer avec succes !"

	def connectionUser(self, user_name, user_pass):
		"""	
			La methode de connection de l'utilisateur dans son espace de jeux
			Cette methode prend en paramettre le nom de l'utilisateur 
			et le mot de passe

			Et retourne 'Ok' si les identifiant est bien renseigner 
			=============================================================

		"""
		self.connexion = connexionDataBase()
		self.con = self.connexion[0]
		self.cur = self.connexion[1]
		self.user_connect_name = user_name	
		self.user_connect_pass = user_pass
		self.temp_liste_users = (self.user_connect_name, self.user_connect_pass)


		self.current_user = self.cur.execute("""SELECT * FROM user""")
		self.con.commit()
		
		for self.user in self.current_user:
			if ((self.user[1] == self.user_connect_name) and (self.user[2] == self.user_connect_pass)):
				self.con.close()
				return ("The User is allread in data base")
			else:
				try:
					self.cur.execute(
					"""
					INSERT IN users (u_name, u_password) VALUES (?, ?)
					""", self.temp_liste_users)
					self.con.close()

				except Exception as e:
					return 'Samething  is wrong is you code'
				else:
					return 'Ok'
				finally:
					'Out of method'

#=====================================

# la fonction du creation de la base de donnner

def connexionDataBase():
	"""
		cette fonction permet la connextion à la base de donnee
	"""
	conn = sql.connect("data_base.db")
	cur = conn.cursor()
	out_data = (conn, cur)
	return out_data

def creatTables():
	# creation des table
	connection = sql.connect("data_base.db")
	cur = connection.cursor()
	cur.execute("""
		CREATE TABLE IF NOT EXISTS users (
				u_id INTEGER PRIMARY KEY AUTOINCREMENT,
				u_name TEXT,
				u_password TEXT
			)""")
	connection.commit()
	cur.execute("""
		CREATE TABLE IF NOT EXISTS mission (
				m_id INTEGER PRIMARY KEY AUTOINCREMENT,
				m_name TEXT,
				m_objectif TEXT
			)""")
	connection.commit()

#===========================================
# une simple fonction de recupération des informations de connexions de l'uilisateur
def userCoordonne():
	list_output = []
	user_name = input("Enter your name :")
	user_pass = input("Enter the user pass word :")
	if ((user_name and user_pass) != ""):
		# les codes à exécuté si l'utilisateur rentrer très biens ces donnes
		list_output.append(user_name)
		list_output.append(user_pass)
		return (list_output)
	else:
		return ("Les informations ne son pas remplis completement ")
#==============================================
# La fonctions de verification de présent de l'utilisateur déjà dans la base de donnée
def verifInDataBase(funct):
	user_datas = funct()
	temp_user_name = user_datas[0]
	temp_user_pass = user_datas[1]

	connexion = sql("data_base.db")
	cursor = connexion.cursor()
	cursor.execute("SELECT * FROM users (u_name, u_password)")
	liste_users = cursor.fetchall()
	connexion.commit()
	connexion.close()

	for user in liste_users:
		if (temp_user_name and temp_user_pass) in user:
			return ("this name is already taken by a other player")
		else:
			pass
		
# nous verifions si les tables sont vraiment creer

if __name__ == "__main__":
	

	if len(temp_liste) == 0:
		print("The data base id created")
	else:
		print("The data base is never created")