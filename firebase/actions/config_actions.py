from firebase.actions.database_actions import read_document
from firebase.config.config import Config


def read_config(app, key: str) -> str:
  config_ref = read_document(app, u'CONFIGS', key)
  return Config.from_doc_ref(config_ref).value;
