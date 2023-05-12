import firebase_admin
from firebase_admin import credentials


def initialize_firebase():
  cred = credentials.Certificate('./firebase_credentials.json')
  return firebase_admin.initialize_app(cred)