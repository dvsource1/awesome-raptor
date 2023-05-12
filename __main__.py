from dotenv import load_dotenv
from firebase.actions.database_actions import read_documents
from firebase.actions.initialize_firebase import initialize_firebase
from firebase.actions.message_actions import send_FCM
from firebase.database.initialize_database import initialize_database

from firebase.notification.notification_profile import NotificationProfile


load_dotenv()


def main():
  print("Running main program...")

  app = initialize_firebase()
  # res = initialize_database(app)
  
  notification_profiles = read_documents(app, u'NOTIFICATIONS')
  
  for notofication_profile in notification_profiles:
    notification = NotificationProfile.from_dict(notofication_profile.to_dict())
    response = send_FCM(app, notification)
    print('Successfully sent message:', response)

if __name__ == "__main__":
  main()