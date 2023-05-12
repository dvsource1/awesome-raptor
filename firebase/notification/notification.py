from firebase.notification.notification_data import NotificationData


class Notification:
    def __init__(self, title: str, subtitle: str, body: str, smallIcon: str, data: NotificationData) -> None:
        self.title = title
        self.subtitle = subtitle
        self.body = body
        self.smallIcon = smallIcon
        self.data = data
    
    @staticmethod
    def from_dict(config_dict, allowReference=False):
        return Notification(
            config_dict.get('title'),
            config_dict.get('subtitle'),
            config_dict.get('body'),
            config_dict.get('smallIcon'),
            config_dict.get('data') if allowReference else NotificationData.from_dict(config_dict.get('data').get().to_dict(), allowReference) if 'data' in config_dict else None
        )
    
    def to_dict(self, allowReference=False):
        return {
            'title': self.title,
            'subtitle': self.subtitle,
            'body': self.body,
            'smallIcon': self.smallIcon,
            'data': self.data if allowReference else self.data.to_dict(allowReference) if self.data is not None else None
        }
    
    def __str__(self):
        return (
            f"Notification(\n\t\t"
            f"title='{self.title}', \n\t\t"
            f"subtitle='{self.subtitle}', \n\t\t"
            f"body='{self.body}', \n\t\t"
            f"smallIcon='{self.smallIcon}', \n\t\t"
            f"data={self.data}\n\t"
            f")"
        )
