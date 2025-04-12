import os
import shutil
import logging

logging.basicConfig(level=logging.INFO)

# Define where files should go
file_structure = {
    "app.py": ".",
    "requirements.txt": ".",
    "setup.py": ".",
    "README.md": ".",
    "Dockerfile": ".",
    "StudentsPerformance.csv": "notebook",
    "template.py": ".",  # will be renamed to app.py
    "mlproject_files": "src/mlproject",
    "components_files": "src/mlproject/components",
    "pipeline_files": "src/mlproject/pipelines"
}

# Files to look for (you can add more here)
known_files = {
    "template.py": ("app.py", "."),
    "logger.py": ("logger.py", "src/mlproject"),
    "exception.py": ("exception.py", "src/mlproject"),
    "data_ingestion.py": ("data_ingestion.py", "src/mlproject/components"),
    "data_transformation.py": ("data_transformation.py", "src/mlproject/components"),
    "model_trainer.py": ("model_trainer.py", "src/mlproject/components"),
    "training_pipeline.py": ("training_pipeline.py", "src/mlproject/pipelines"),
    "prediction_pipeline.py": ("prediction_pipeline.py", "src/mlproject/pipelines"),
}

# Move files to correct location
for old_name, (new_name, target_dir) in known_files.items():
    if os.path.exists(old_name):
        os.makedirs(target_dir, exist_ok=True)
        new_path = os.path.join(target_dir, new_name)
        logging.info(f"Moving {old_name} → {new_path}")
        shutil.move(old_name, new_path)

logging.info("✅ Project auto-organized successfully!")
