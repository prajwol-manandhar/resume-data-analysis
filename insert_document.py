
from firebase_admin import firestore

def insert_user():

    res = firestore.client().collection('user').document('emilywatson').set({
      'id': 'emilywatson',
      'location': 'Sydney',
      'phone': '',
      'email': 'emilywatson@gmail.com',
      'skills': ['Python', 'NodeJS']
    })