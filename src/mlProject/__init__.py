import os 
import sys
import logging


logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s]"

log_dir = 'logs'
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,
    handlers=[logging.FileHandler(log_filepath),    #se usa para guardar los logs en un archivo
              logging.StreamHandler(sys.stdout)]    # se usa para mostrar los logs en la consola
)

logger = logging.getLogger("mlProjectLogger")       # Crear un logger personalizado con un nombre específico