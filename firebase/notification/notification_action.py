class NotificationAction:
    def __init__(self, key: str, description: str, datatype: str, cron: str) -> None:
        self.key = key
        self.description = description
        self.datatype = datatype
        self.cron = cron
    
    @staticmethod
    def from_dict(action_dict):
        return NotificationAction(
            action_dict['key'],
            action_dict['description'],
            action_dict['datatype'],
            action_dict['cron']
        )
    
    def to_dict(self):
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
