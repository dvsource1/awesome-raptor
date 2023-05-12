from firebase.database.document import FirebaseDocument


class NotificationAction(FirebaseDocument):
    def __init__(self, key: str, description: str, datatype: str, cron: str) -> None:
        super().__init__(key)
        self.description = description
        self.datatype = datatype
        self.cron = cron
    
    @staticmethod
    def from_dict(action_dict, allowReference=False):
        return NotificationAction(
            action_dict.get('key'),
            action_dict.get('description'),
            action_dict.get('datatype'),
            action_dict.get('cron')
        )
    
    def to_dict(self, allowReference=False):
        return {
            'key': self.key,
            'description': self.description,
            'datatype': self.datatype,
            'cron': self.cron
        }
    
    def __str__(self):
        return (
            f"NotificationAction(\n\t\t"
            f"key='{self.key}', \n\t\t"
            f"description='{self.description}', \n\t\t"
            f"datatype='{self.datatype}', \n\t\t"
            f"cron='{self.cron}'\n\t"
            f")"
        )
