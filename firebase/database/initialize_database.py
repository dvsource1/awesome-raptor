from firebase.actions.database_actions import create_document, create_documents, delete_collection
from firebase.config.config import Config
from firebase.notification.notification import Notification
from firebase.notification.notification_action import NotificationAction
from firebase.notification.notification_data import NotificationData
from firebase.notification.notification_profile import NotificationProfile


def initialize_collection(app, collection, documents):
  delete_collection(app, collection)
  return create_documents(app,collection, documents)


def initialize_configs(app, collection):
  CONFIGS = [
    Config.from_dict({'key': 'FCM_TOKEN', 'value': 'ABCD'})
  ]
  return initialize_collection(app, collection, CONFIGS)

def initialize_actions(app, collection):
  ACTIONS = [
    NotificationAction.from_dict({'key': 'CURRENT_TOP_VALUE', 'cron': '* * * * *'})
  ]
  return initialize_collection(app, collection, ACTIONS)

def initialize_data(app, collection):
  DATA = [
    NotificationData.from_dict({'key': 'BINANCE_P2P_TOP_USDT_BUYER_RATE', 'value': '1234'})
  ]
  return initialize_collection(app, collection, DATA)


def initialize_database(app):
  config_refs = initialize_configs(app, u'TEST_CONFIGS')
  action_refs = initialize_actions(app, u'TEST_ACTIONS')
  data_refs = initialize_data(app, u'TEST_DATA')
  
  # NOTIFICATIONS
  NOTIFICATION_PROFILES = [
    NotificationProfile.from_dict({
      'key': 'BINANCE_P2P_TOP_USDT_BUYER_RATE',
      'action': action_refs.get('CURRENT_TOP_VALUE'),
      'notification': {
        'title': 'Hi!',
        'body': 'Test Notification',
        'smallIcon': 'ic_launcher',
        'data': data_refs.get('BINANCE_P2P_TOP_USDT_BUYER_RATE')
      }
    }, allowReference=True)
  ]
  notification_refs = initialize_collection(app, u'TEST_NOTIFICATION_PROFILES', NOTIFICATION_PROFILES)
  
  return [config_refs ,action_refs, data_refs, notification_refs]
