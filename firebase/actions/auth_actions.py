import os
import requests
from firebase_admin import auth


FIREBASE_RERT_APIKEY = os.getenv('FIREBASE_RERT_APIKEY')
FIREBASE_AUTH_EMAIL = os.getenv('FIREBASE_AUTH_EMAIL')
FIREBASE_AUTH_PASSWORD = os.getenv('FIREBASE_AUTH_PASSWORD')


def firebase_authenticate():
  payload = {'email': FIREBASE_AUTH_EMAIL, 'password': FIREBASE_AUTH_PASSWORD, 'returnSecureToken': True}
  res = requests.post(f'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_RERT_APIKEY}', data=payload)
  
  id_token = res.json()['idToken']
  user = auth.verify_id_token(id_token)
  return id_token, user
