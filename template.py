import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_file(filepath):
    """Create a file if it doesn't exist or is empty."""
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as file:
            pass
        logger.info(f"Created file: {filepath}")

def create_directory_if_not_exists(directory):
    """Create a directory if it doesn't exist."""
    if not directory.exists():
        directory.mkdir(parents=True, exist_ok=True)
        logger.info(f"Created directory: {directory}")

def create_files(file_paths):
    """Create files and their parent directories."""
    for file_path in file_paths:
        file_path = Path(file_path)
        create_directory_if_not_exists(file_path.parent)
        create_file(file_path)

if __name__ == "__main__":
    list_of_files = [
        ".github/workflows/.gitkeep",
        "src/__init__.py",
        "src/components/__init__.py",
        "src/components/data_ingestion.py",
        "src/components/data_transformation.py",
        "src/components/model_trainer.py",
        "src/components/model_evaluation.py",
        "src/pipeline/__init__.py",
        "src/pipeline/training_pipeline.py",
        "src/pipeline/prediction_pipeline.py",
        "src/utils/__init__.py",
        "src/utils/utils.py",
        "src/logger/logging.py",
        "src/exception/exception.py",
        "src/mongo_connect/__init__.py",  # Add this line
        "src/mongo_connect/mongo_crud.py",  # Add this line
        "tests/integration/__init__.py",
        "tests/integration/test_int.py",
        "tests/unit/__init__.py",
        "tests/unit/test_unit.py",
        "init_setup.sh",
        "requirements.txt",
        "requirements_dev.txt",
        "setup.py",
        "setup.cfg",
        "pyproject.toml",
        "tox.ini",
        "experiment/experiments.ipynb"
    ]

    create_files(list_of_files)
