import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s]: %(message)s"
    )

while True:
    project_name = input("Enter project name: ")
    if project_name != "":
        break

logging.info(f"creating project by name {project_name}")

# list of files:
list_of_files = [
    f"src/{project_name}/__init__.py",
]

for filepath in list_of_files:
    filedir, filename = os.path.split(Path(filepath))
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"created directory {filedir} for file {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"created file {filename} at {filepath}")
    else:
        logging.info(f"file {filename} already exists at {filepath}")