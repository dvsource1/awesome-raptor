from firebase.notification.notification import Notification
from firebase.notification.notification_action import NotificationAction


class NotificationProfile:
    def __init__(self, name: str, code: str, description: str, action: NotificationAction, notification: Notification) -> None:
        self.name = name
        self.code = code
        self.description = description
        self.action = action
        self.notification = notification

    @staticmethod
    def from_dict(source_dict):
        return NotificationProfile(
            source_dict['name'],
            source_dict['code'],
            source_dict['description'],
            NotificationAction.from_dict(source_dict['action'].get().to_dict()),
            Notification.from_dict(source_dict['notification'])
        )
        
    def from_doc_ref(doc_ref):
        doc = doc_ref.get()
        return NotificationProfile.from_dict(doc.to_dict())
    
    def to_dict(self):
        return {
            'name': self.name,
            'code': self.code,
            'description': self.description,
            'action': self.action,
            'notification': self.notification,
        }
        
    def __str__(self):        
        return (
            f"NotificationProfile(\n\t"
            f"name='{self.name}', \n\t"
            f"code='{self.code}', \n\t"
            f"description='{self.description}', \n\t"
            f"action='{self.action}', \n\t"
            f"notification='{self.notification}'\n"
            f")"
        )





