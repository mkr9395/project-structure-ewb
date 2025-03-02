## 1. Project Skeleton:

```
my_ml_project/
│
├── data/
│   ├── raw/                 # Raw, unprocessed data
│   ├── processed/           # Preprocessed/cleaned data
│   ├── external/            # External datasets, if any
│   └── interim/             # Intermediate data processing results
│
├── notebooks/               # Jupyter notebooks for exploration and EDA
│   ├── 01_data_exploration.ipynb
│   └── 02_model_building.ipynb
│
├── src/                     # Source code for the project
│   ├── __init__.py          # Marks this as a Python package
│   ├── data/                # Data ingestion, preprocessing scripts
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   └── data_cleaning.py
│   ├── features/            # Feature engineering scripts
│   │   ├── __init__.py
│   │   └── feature_engineering.py
│   ├── models/              # Model training and inference scripts
│   │   ├── __init__.py
│   │   ├── train.py
│   │   └── predict.py
│   ├── evaluation/          # Model evaluation scripts
│   │   ├── __init__.py
│   │   └── evaluate.py
│   ├── utils/               # Utility functions (e.g., logging, helpers)
│   │   ├── __init__.py
│   │   ├── setup_logging.py
│   │   └── helper_functions.py
│   └── config/              # Configuration files
│       └── config.yaml      # Configuration settings for the project
│
├── models/                  # Folder for saving trained models
│   └── model.pkl            # Saved model after training
│
├── logs/                    # Log files from training and evaluation
│   └── training.log
│
├── scripts/                 # Shell or batch scripts for running workflows
│   └── train_model.sh
│
├── tests/                   # Unit and integration tests
│   ├── __init__.py          # Marks the tests folder as a Python package
│   ├── test_data_ingestion.py
│   └── test_train.py
│
├── artifacts/               # Store generated artifacts (plots, reports)
│   ├── __init__.py
│   ├── figures/             # Visualizations, graphs, etc.
│   └── reports/             # Performance metrics, etc.
│
├── docs/                    # Project documentation
│   ├── api.md
│   └── installation.md
│
├── visualizations/          # Data visualizations (plots, graphs, etc.)
│   └── eda_plots/
│
├── references/              # External papers, resources, etc.
│   └── paper.pdf
│
├── experiments/             # Tracking experiment results (metrics, etc.)
│   └── run_01/metrics.json
│
├── requirements.txt         # Python package requirements
├── environment.yml          # Conda environment file
├── README.md                # Project documentation
├── setup.py                 # Installation script for the project (optional)
└── .gitignore               # Files and folders to ignore in version control
```

### Explanation of the Folders and Files:

1. **`data/`**: Stores all datasets.
   - `raw/`: Raw data, as received (e.g., downloaded from sources).
   - `processed/`: Data that has been cleaned and preprocessed.
   - `external/`: Any external data sources.

2. **`notebooks/`**: Contains exploratory Jupyter notebooks used for initial data exploration, EDA (Exploratory Data Analysis), and prototyping models.

3. **`src/`**: The core source code directory for the project.
   - `data/`: Scripts to load, clean, and preprocess data.
   - `features/`: Scripts for feature engineering.
   - `models/`: Scripts for training and predicting using machine learning models.
   - `evaluation/`: Scripts for evaluating model performance.
   - `utils/`: Helper functions and logging setup.
   - `config/`: Configuration files for the project (e.g., paths, hyperparameters).

4. **`models/`**: Stores trained models (e.g., `.pkl` files).

5. **`logs/`**: Log files for tracking progress during training and evaluation.

6. **`scripts/`**: Useful shell or batch scripts to automate workflows (e.g., `bash train_model.sh` to run the training pipeline).

7. **`tests/`**: Unit tests and integration tests for ensuring your code is functioning as expected.

8. **`artifacts/`**: Contains generated outputs such as visualizations, plots, and reports (e.g., feature importance plots, confusion matrices).

9. **`requirements.txt`**: List of dependencies required for the project if using `pip`.

10. **`environment.yml`**: Conda environment file to capture all dependencies and their versions (useful for setting up reproducible environments).

11. **`README.md`**: A project overview and instructions for setup, usage, and deployment.

12. **`setup.py`**: Installation script for the project, useful if the project will be installed as a Python package.

13. **`.gitignore`**: Specifies which files/folders Git should ignore (e.g., large data files, logs, etc.).


- **`params.yaml`**: Stores hyperparameters and configuration settings for model training and experimentation.
- **`environment.yaml`**: Defines the Conda environment with package dependencies for the project.
- **`schema.yaml`**: Contains schema definitions for data validation, ensuring correct data formats.
- **`main.py`**: The entry point for the core logic of the machine learning pipeline or application.
- **`app.py`**: The application script, typically used for serving the model (e.g., in a web API using Flask/FastAPI).
- **`Dockerfile`**: Instructions to build a Docker image for containerizing the application.
- **`templates/index.html`**: HTML template for the web interface, often used with Flask or FastAPI apps.
- **`test.py`**: A testing script to validate the functionality of the project components.


### Deployment Considerations:
- **Dockerfile**: If containerizing, consider adding a `Dockerfile` for creating a reproducible environment.
- **CI/CD Pipelines**: Add configuration for continuous integration (e.g., GitHub Actions, Travis CI) if needed for automated testing and deployment.

This structure allows for a clean, organized workflow and prepares the project for seamless deployment. 

================================================================

## 2. Virtual env and requirements.txt

1. Create new Environment

conda create -p env python=3.9 -y

2. Activate your environment

conda activate env/ -> CMD

source activate env/ -> Git bash

3. Install your requriments file

pip install -r requirements.txt

==============================================================

## 3. Set up setup.py

1. Import the important libraries

2. Write the entire setup.py files

3. add "-e ." in requirements.txt files

4. do `pip install -r requirements.txt`

============================================================

## 4. Initialising MongoDB

1. Website : https://cloud.mongodb.com/
2. Create a project and inside the project create a cluster.
3. For free services use M0
4. Create a user and password and create database user. Then choose a connection method.
5. select "Drivers" in connect your application
6. Set Driver as "python" and Version as "3.6 or later"
7. Download the dataset.
8. Convert the csv dataset into dictionary in **("key" : "value")** format
   > `data = df.to_dict(orient="records")`
9. Connection should be made to mondb cluster and data will be sent.

============================================================
## 5. Write logging exception and utils module

1. logging of logs started in logs folder
2. logging script was written in logger folder's __init__.py files
3. and imported inside the demo.py files to check whether logging is working
4. `python-box` library will handle Exception handling : `BoxValueError` 
   -> `from box.exceptions import BoxValueError`
   -> `BoxValueError` is effective and sufficient for handling exceptions related to `Box` operations.
5. common functionalities will be written in utils/common.py file
6. `@ensure_annotations` : operation will only perform if correct data type variable is passed.
7.`ConfigBox` : helps to fetch values from dictionary using "." `dict.key` method instead of calling by `dict['key']`
8. Custom exceptions created in `src/exceptions/__init__.py` file and tested in  `demo.py` file

============================================================

## 6. 






#### Anaconda: https://www.anaconda.com/
- Vs code: https://code.visualstudio.com/download
- Git: https://git-scm.com/
- Flowchart: https://whimsical.com/
- MLOPs Tool: https://www.evidentlyai.com/
- MongoDB: https://account.mongodb.com/account/login
- Dataset url: https://www.kaggle.com/datasets/moro23/easyvisa-dataset