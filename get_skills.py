from firebase_admin import firestore

def user_skills():
    users_ref = firestore.client().collection('user')
    docs = users_ref.stream()
    for doc in docs:
        skills = u'{}'.format(doc.to_dict()['skills'])
        print(skills)