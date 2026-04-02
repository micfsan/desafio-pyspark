import yaml
import os

class ConfigManager:

    def __init__(self, path: str = "config/settings.yaml"):
        self.path = path
        if not os.path.exists(self.path):
            self.path = os.path.join(os.getcwd(), "config/settings.yaml")
        
        self.config = self._load()

    def _load(self) -> dict:
        """Método privado para carregar o arquivo."""
        with open(self.path, "r") as file:
            return yaml.safe_load(file)

    def get_config(self) -> dict:
        """Retorna o dicionário de configurações para o Aggregation Root."""
        return self.config
