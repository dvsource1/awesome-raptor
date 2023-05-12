from firebase.database.document import FirebaseDocument
from firebase.notification.notification import Notification
from firebase.notification.notification_action import NotificationAction


class NotificationProfile(FirebaseDocument):
    def __init__(self, key, name: str, code: str, description: str, action: NotificationAction, notification: Notification) -> None:
        super().__init__(key)
        self.name = name
        self.code = code
        self.description = description
        self.action = action
        self.notification = notification

    @staticmethod
    def from_dict(source_dict, allowReference=False):
        return NotificationProfile(
            source_dict.get('key'),
            source_dict.get('name'),
            source_dict.get('code'),
            source_dict.get('description'),
            source_dict.get('action') if allowReference else NotificationAction.from_dict(source_dict['action'].get().to_dict(), allowReference) if 'action' in source_dict else None,
            Notification.from_dict(source_dict.get('notification', {}), allowReference)
        )
    
    def to_dict(self, allowReference=False):
        return {
            'key': self.key,
            'name': self.name,
            'code': self.code,
            'description': self.description,
            'action': self.action if allowReference else self.action.to_dict(allowReference) if self.action is not None else None,
            'notification': self.notification.to_dict(allowReference) if self.notification is not None else None,
        }
        
    def __str__(self):        
        return (
            f"NotificationProfile(\n\t"
            f"key='{self.key}', \n\t"
            f"name='{self.name}', \n\t"
            f"code='{self.code}', \n\t"
            f"description='{self.description}', \n\t"
            f"action='{self.action}', \n\t"
            f"notification='{self.notification}'\n"
            f")"
        )





