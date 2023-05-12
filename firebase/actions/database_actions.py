from firebase_admin import firestore


def read_documents(app, collection: str):
  db = firestore.client(app)
  return db.collection(collection).list_documents()


def read_document(app, collection: str, document: str):
  db = firestore.client(app)
  return db.collection(collection).document(document);