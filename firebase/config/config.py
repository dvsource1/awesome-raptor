from firebase.database.document import FirebaseDocument


class Config(FirebaseDocument):
  def __init__(self, key: str, description: str, value: str, initial_value: str) -> None:
    super().__init__(key)
    self.description = description
    self.value = value
    self.initial_value = initial_value
    
  @staticmethod
  def from_dict(config_dict, allowReference=False):
      return Config(
          config_dict.get('key'),
          config_dict.get('description'),
          config_dict.get('value'),
          config_dict.get('initial_value'),
      )
    
  def to_dict(self, allowReference=False):
      return {
          'key': self.key,
          'description': self.description,
          'value': self.value,
          'initial_value': self.initial_value,
      }
    
  def __str__(self):
      return (
          f"Config(\n\t"
          f"key='{self.key}', \n\t"
          f"description='{self.description}', \n\t"
          f"value='{self.value}', \n\t"
          f"initial_value='{self.initial_value}', \n"
          f")"
      )
