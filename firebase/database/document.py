from abc import ABC, abstractmethod


class FirebaseDocument(ABC):
  def __init__(self, key: str) -> None:
    self.key = key
    
  @classmethod
  @staticmethod
  def from_dict(source, allowReference=False) -> 'FirebaseDocument':
    pass

  @abstractmethod
  def to_dict(self, allowReference=False) -> dict:
    pass