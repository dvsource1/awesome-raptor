class Config:
  def __init__(self, key: str, description: str, value: str, initial_value: str) -> None:
    self.key = key
    self.description = description
    self.value = value
    self.initial_value = initial_value
    
  @staticmethod
  def from_dict(config_dict):
      return Config(
          config_dict['key'],
          config_dict['description'],
          config_dict['value'],
          config_dict['initial_value'],
      )

  @staticmethod
  def from_doc_ref(doc_ref):
    doc = doc_ref.get()
    return Config.from_dict(doc.to_dict())
    
  def to_dict(self):
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
