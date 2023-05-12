import datetime

class NotificationData:
    def __init__(self, key: str, description: str, value: str, initial_value: str, last_updated: datetime.datetime) -> None:
        self.key = key
        self.description = description
        self.value = value
        self.initial_value = initial_value
        self.last_updated = last_updated
    
    @staticmethod
    def from_dict(data_dict):
        return NotificationData(
            data_dict['key'],
            data_dict['description'],
            data_dict['value'],
            data_dict['initial_value'],
            data_dict['last_updated']
        )
    
    def to_dict(self):
        return {
            'key': self.key,
            'description': self.description,
            'value': self.value,
            'initial_value': self.initial_value,
            'last_updated': self.last_updated
        }
        
    def to_str_dict(self):
        return {
            'key': self.key,
            'description': self.description,
            'value': str(self.value),
            'initial_value': str(self.initial_value),
            'last_updated': self.last_updated.isoformat()
        }
        
    def __str__(self):
        return (
            f"NotificationData(\n\t\t\t"
            f"key='{self.key}', \n\t\t\t"
            f"description='{self.description}', \n\t\t\t"
            f"value='{self.value}', \n\t\t\t"
            f"initial_value='{self.initial_value}', \n\t\t\t"
            f"last_updated={self.last_updated.isoformat()}\n\t\t"
            f")"
        )
