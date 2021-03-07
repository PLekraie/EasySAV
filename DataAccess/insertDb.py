from dbConnect import DbConnect
from Domain.intervention import Intervention

################################################
# that file should care of database operations #
################################################

# Objet à insérer
# inter2 = Intervention("Television ecran vert", "Passif")

# get database connexion
connexion = DbConnect("EasyDb").getconnection()
curseur = connexion.cursor()

cmd = f"select * from Intervention"

curseur.execute(cmd)
connexion.commit()
