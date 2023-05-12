from typing import List
from firebase_admin import firestore

from firebase.database.document import FirebaseDocument


def read_documents(app, collection: str) -> List[FirebaseDocument]:
  db = firestore.client(app)
  return db.collection(collection).stream()


def read_document(app, collection: str, document: str) -> FirebaseDocument:
  db = firestore.client(app)
  return db.collection(collection).document(document).get()


def create_documents(app, collection: str, documents: List[FirebaseDocument]):
  db = firestore.client(app)
  batch = db.batch()
  
  doc_refs = {}
  for document in documents:
    if document.key is not None:
      doc_ref = db.collection(collection).document(document.key)
      doc_refs[document.key] = doc_ref
    else:
      doc_ref = db.collection(collection).document()
    batch.set(doc_ref, document.to_dict(allowReference=True))

  batch.commit()
  return doc_refs


def create_document(app, collection: str, document: FirebaseDocument):
  db = firestore.client(app)
  
  doc_ref = db.collection(collection).document(document.key if document.key is not None else None)
  doc_ref.set(document.to_dict())
  return doc_ref


def update_document(app, collection: str, document: FirebaseDocument):
  db = firestore.client(app)
  
  if document is not None:
    doc_ref = db.collection(collection).document(document.key)
    doc_ref.update(document.to_dict())
    return doc_ref
  else:
    return create_document(app, collection, document)


def delete_collection(app, collection: str):
  db = firestore.client(app)
  doc_refs = db.collection(collection).list_documents()
  for doc_ref in doc_refs:
    doc_ref.delete()
