import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    ".github/workflows/.gitkeep",
    f"docs/",
    
    f"data/raw/",
    f"data/interim/",
    f"data/processed/",
    f"data/external/",
    f"data/__init__.py",
    
    f"src/__init__.py",
    
    f"src/data/__init__.py", # data -> components, data_ingestion,preeprocessing
    
    f"src/entity/__init__.py",
    f"src/entity/config_entity.py", 
    
    f"src/features/__init__.py",
    
    f"src/models/__init__.py", # Model training and inference scripts
    
    f"src/evaluation/__init__.py",
    
    f"src/utils/__init__.py", # utils is used for logging and helper
    f"src/utils/common.py",
    
    f"src/logger/__init__.py",
    
    f"src/config/config.yaml", # Configuration settings for the project
    # "config/configuration.py", 
    
    f"notebooks/__init__.py", # notebooks -> constants
    
    f"models/",
    
    f"logs/",
    
    f"tests/__init__.py",  # Unit and integration tests
    
    f"artifacts/__init__.py",
    f"artifacts/figures/",
    f"artifacts/reports/",
    
    "params.yaml",
    "environment.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "templates/index.html",
    "test.py"
    "dvc.yaml"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} already exists")
        
    project_root = Path(__file__).resolve().parent    
    data_folders = [
       project_root / "data" / "raw",
        project_root / "data" / "interim",
        project_root / "data" / "processed"
    ]
    
    # Create the directories if they don't exist
    for folder in data_folders:
        folder.mkdir(parents=True, exist_ok=True)  # Create directories, including any parent dirs
        print(f"Created or exists: {folder}")