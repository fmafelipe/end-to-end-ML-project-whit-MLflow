# Utils se usa para funcionalidades comunes de uso frecuente (como para leer un YAML) que pueden ser utilizadas en diferentes partes del proyecto

import os 
import yaml
from mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """ lee archivo yaml y retorna
    
    Args: 
        path_to_yaml (str): ruta al archivo yaml

    Raises
        ValueError: si el archivo yaml esta vacio
        e: empty file

    Return 
        ConfigBox: ConfigBox type    
    """


    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """ Crea una lista de directorios (carpetas)
    
    Args:
        path_to_directories (list): lista de rutas de los directorios
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")    


@ensure_annotations
def save_json(path: Path, data: dict):
    """ Guarda un arhivo json
    
    Args:
        path (Path): ruta al archivo json a guardar
        data (dict): datos en formato diccionario a guardar en json
    """

    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Lee archivos json

    Args:
        path (Path): ruta al archivo json a leer
    Returns:
        ConfigBox: datos como un objeto de tipo ConfigBox
    """
    with open(path) as f:
        content = json.load(f)
    
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path:Path):
    """ Guarda un arhivo binario usando joblib
    
    Args:
        data (Any): datos a guardar como un binario
        path (Path): ruta al archivo binario a guardar
    """ 
    joblib.dump(data, path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path:Path) -> Any:
    """ Lee un archivo binario usando joblib
    
    Args:
        path (Path): ruta al archivo binario a leer

    Returns:
        Any: datos leidos del archivo binario
    """ 
    data = joblib.load(path)
    logger.info(f"binary file loaded successfully from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """ Obtiene el tamaño de un arhivo en Kb
    Args:
        path (Path): ruta al archivo
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

