from pathlib import Path
import os
import logging

# List of files and directories to be created
list_of_files = [
    ".github/workflows/.gitkeep",
    "docs/",
    
    "data/raw/",
    "data/interim/",
    "data/processed/",
    "data/external/",
    "data/__init__.py",
    
    "src/__init__.py",
    "src/data/__init__.py",
    "src/entity/__init__.py",
    "src/entity/config_entity.py",
    
    "src/features/__init__.py",
    "src/models/__init__.py",
    "src/evaluation/__init__.py",
    
    "src/utils/__init__.py",
    "src/utils/common.py",
    
    "src/logger/__init__.py",
    
    "src/config/config.yaml",
    
    "notebooks/__init__.py",
    
    "models/",
    
    "logs/",
    
    "tests/__init__.py",
    
    "artifacts/__init__.py",
    "artifacts/figures/",
    "artifacts/reports/",
    
    "params.yaml",
    "environment.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "templates/index.html",
    "test.py",
    "dvc.yaml",
    "demo.py"
]

# Function to create directories and files
def create_project_structure(file_list):
    for filepath in file_list:
        filepath = Path(filepath)  # Convert to pathlib Path object
        
        if filepath.suffix:  # If it has a suffix, it's a file
            filedir = filepath.parent  # Get the directory part of the path
            if not filedir.exists():
                filedir.mkdir(parents=True, exist_ok=True)
                logging.info(f"Creating directory: {filedir} for the file: {filepath.name}")
            if not filepath.exists():
                filepath.touch()  # Create an empty file
                logging.info(f"Creating empty file: {filepath}")
        else:  # It's a directory if it doesn't have a suffix
            if not filepath.exists():
                filepath.mkdir(parents=True, exist_ok=True)
                logging.info(f"Creating directory: {filepath}")

# Run the function to create project structure
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    create_project_structure(list_of_files)
