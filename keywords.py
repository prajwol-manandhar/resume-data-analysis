import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("service_key.json")

db = firestore.client()

def tech_keywords():
    keywords_ref = db.collection('keyword')
    docs = keywords_ref.stream()
    for doc in docs:
        keywords = u'{}'.format(doc.to_dict()['technology'])
        print(keywords)