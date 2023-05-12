from dotenv import load_dotenv
from firebase.actions.database_actions import read_documents
from firebase.actions.initialize_firebase import initialize_firebase
from firebase.actions.message_actions import send_FCM

from firebase.notification.notification_profile import NotificationProfile


load_dotenv()


def main():
  print("Running main program...")

  app = initialize_firebase()
  
  notofication_profile_refs = read_documents(app, u'NOTIFICATIONS')
  
  for notofication_profile_ref in notofication_profile_refs:
    notification = NotificationProfile.from_doc_ref(notofication_profile_ref)
    response = send_FCM(app, notification)
    print('Successfully sent message:', response)

if __name__ == "__main__":
  main()