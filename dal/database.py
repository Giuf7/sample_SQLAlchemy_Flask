from datetime import datetime
import os
from contextlib import contextmanager
from dal.models.base import Base
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from dal.models.task import Task

load_dotenv()

DATABASE_URL = os.getenv(
	"CONNECTION_STRING"
)

engine = create_engine(
	DATABASE_URL,
	echo=False
)

session_local = sessionmaker(autocommit=False ,autoflush=False ,bind=engine)


def init_db(delete=False):
	if delete:
		Base.metadata.drop_all(bind=engine)
		print("❌ - Toutes les tables on été supprimées.")
	Base.metadata.create_all(bind=engine)
	print("✅ - Tables créées / mise à jour.")

def test_connexion():
	try:
		with engine.connect() as conn:
			conn.execute(text("SELECT 1"))
			print("✅ Connexion établie à SQL Server 😊")
			return True
	except Exception as e:
		print(f"❌ Erreur de connexion : {e}")
		return False

# Exemple seed data

# def seed_data():
# 	with get_db() as db:
# 		if db.query(Task).count() == 0:
# 			now = datetime.now()
# 			demo_taks = [
# 				Task(
# 					titre= "Apprendre Flask",
# 					description= "suivre les cours à tf",
# 					done= False
# 				),
# 				Task(
# 					titre= "Apprendre SQl",
# 					description= "suivre les cours à tf",
# 					done= False
# 				),
# 				Task(
# 					titre= "Apprendre SQl",
# 					description= "suivre les cours à tf",
# 					done= False,
# 					created_at= now,
# 					updated_at= now
# 				)
# 			]
# 			db.add_all(demo_taks)
# 			print("[✅] Seed data ajouté !!!")



@contextmanager
def get_db():
	db = session_local()
	try:
		yield db
		db.commit()
	except Exception:
		db.rollback()
		raise
	finally:
		db.close()