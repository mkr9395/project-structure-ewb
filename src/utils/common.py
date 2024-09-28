import os
from box.exceptions import BoxValueError
from box import config_box
import yaml
import json
import dill
from pandas import DataFrame
import joblib
from pathlib import Path
from ensure import ensure_annotations
from typing import Any
import base64

from logger import logging
from src.exceptions import USvisaException

@ensure_annotations
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    """reads yaml file and returns
    Args:
        path_to_yaml (str): path like input
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file : {path_to_yaml} loaded succesfully")
            return Config_box(content)
    except BoxValueError:
        raise ValueError(f"Empty yaml file at {path_to_yaml}")
    except Exception as e:
        raise e

@ensure_annotations   
def create_directories(path_to_directories : list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data:dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path,'w') as f:
        json.dump(data, f, indent=4)
        
    logger.info(f"json file : {path} saved successfully")
        

@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        data = json.load(f)
    logger.info(f'json file loaded succesfully from : {path}')   
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path:Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    try:
        joblib.dump(value=data, filename=path)
        logger.info(f"binary file saved at : {path}")
    except Exception as e:
        raise USvisaException(e, sys) from e
    


def load_bin(path:Path)->Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    try:
        data = joblib.load(path)
        logger.info(f"binary files loaded from {path}")
        return data
    except Exception as e:
        raise USvisaException(e, sys) from e
    
# from e: Links the new exception (USvisaException) to the original exception (e). 
# It establishes a clear chain of exceptions and allows you to trace back what caused the new exception.



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

@ensure_annotations
def save_numpy_array_data(file_path: str, array: np.array):
    """
    Save numpy array data to file
    file_path: str location of file to save
    array: np.array data to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise USvisaException(e, sys) from e
    
@ensure_annotations
def load_numpy_array_data(file_path: str) -> np.array:
    """
    load numpy array data from file
    file_path: str location of file to load
    return: np.array data loaded
    """
    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise USvisaException(e, sys) from e
    
    
@ensure_annotations 
def drop_columns(df: DataFrame, cols: list)-> DataFrame:

    """
    drop the columns form a pandas DataFrame
    df: pandas DataFrame
    cols: list of columns to be dropped
    """
    logging.info("Entered drop_columns methon of utils")

    try:
        df = df.drop(columns=cols, axis=1)

        logging.info("Exited the drop_columns method of utils")
        
        return df
    except Exception as e:
        raise USvisaException(e, sys) from e
    
def load_object(file_path: str) -> object:
    logging.info("Entered the load_object method of utils")

    try:

        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)

        logging.info("Exited the load_object method of utils")

        return obj

    except Exception as e:
        raise USvisaException(e, sys) from e