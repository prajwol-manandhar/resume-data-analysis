import firebase_admin
from firebase_admin import credentials

from analysis import get_user_skills, get_tech_result, get_management_result, get_softskill_result, feedback

cred = credentials.Certificate("service_key.json")
firebase_admin.initialize_app(cred)

userid = input('Please enter the userID: ')

user_skill_string = get_user_skills(userid)
tech_result = get_tech_result(user_skill_string)
management_result = get_management_result(user_skill_string)
softskill_result = get_softskill_result(user_skill_string)

feedback(tech_result, management_result, softskill_result)
