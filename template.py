import os
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

import os
import logging
from pathlib import Path

# Setup logging to print messages in the terminal
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Optional: quick check to see script is running
print("Template script is running...")

# Define your project name
project_name = "cnnClassifier"

# List of files to create
list_of_files = [ ".github/workflows/.gitkeep",f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

# Loop through each file
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directory if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Directory created (or exists): {filedir}")

    # Create empty file if it doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Empty file created: {filepath}")
    else:
        logging.info(f"File already exists: {filename}")
