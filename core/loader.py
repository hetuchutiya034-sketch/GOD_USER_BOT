import os
from core.logger import log

def load_plugins():
    plugins = os.listdir("plugins")
    for file in plugins:
        if file.endswith(".py"):
            log(f"Loaded Plugin: {file}")
