from firebase.notification.notification_data import NotificationData


class Notification:
    def __init__(self, title: str, subtitle: str, body: str, smallIcon: str, data: NotificationData) -> None:
        self.title = title
        self.subtitle = subtitle
        self.body = body
        self.smallIcon = smallIcon
        self.data = data
    
    @staticmethod
    def from_dict(config_dict):
        return Notification(
            config_dict['title'],
            config_dict['subtitle'],
            config_dict['body'],
            config_dict['smallIcon'],
            NotificationData.from_dict(config_dict['data'].get().to_dict())
        )
    
    def to_dict(self):
        return {
            'title': self.title,
            'subtitle': self.subtitle,
            'body': self.body,
            'smallIcon': self.smallIcon,
            'data': self.data
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
