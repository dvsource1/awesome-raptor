import json
from firebase_admin import messaging

from firebase.actions.config_actions import read_config
from firebase.notification.notification_profile import NotificationProfile


def create_notiffication(title: str, body: str, image=None) -> messaging.Notification:
  return messaging.Notification(title=title, body=body, image=image)
  

def create_cloud_message(token: str, notification: messaging.Notification, data: dict = None) -> messaging.Message:
  return messaging.Message(notification=notification, data=data, token=token)


def send_FCM(app, notification_profile: NotificationProfile) -> str:
  fcm_token = read_config(app, u'FCM_TOKEN')
  notification = create_notiffication(notification_profile.notification.title, notification_profile.notification.body)
  message_data = notification_profile.notification.data.to_str_dict()
  message = create_cloud_message(fcm_token, notification, message_data)
  
  # return '-1'
  return messaging.send(message)
