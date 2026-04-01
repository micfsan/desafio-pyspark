import yaml
import os


def load_config(path: str = "config/settings.yaml") -> dict:
    """Carrega o arquivo de configuração YAML."""
    if not os.path.exists(path):
        # Fallback para caso o caminho precise de ajuste no ambiente
        path = os.path.join(os.getcwd(), "config/settings.yaml")

    with open(path, "r") as file:
        return yaml.safe_load(file)
