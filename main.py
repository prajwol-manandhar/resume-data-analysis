import firebase_admin
from firebase_admin import credentials

#from insert_document import insert_user
from get_skills import user_skills
#from keywords import tech_keywords

cred = credentials.Certificate("service_key.json")
firebase_admin.initialize_app(cred)

user_skills()