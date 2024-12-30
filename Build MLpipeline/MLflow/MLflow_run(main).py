"""
Example of define a main script for MLflow pipeline
"""
import mlflow
"""
mlflow.run(
  # URI can be a local path or the URL to a git repository
  # path of the folder containing the MLflow project(script,project description and environment description)
  uri="my_project",
  # Entry point to call
  entry_point="main",
  # Parameters for that entry point
  parameters={
    "file_url": "https://...",
    "artifact_name": "my_data.csv"
  }
)
"""
#Run the first component(download_data)
mlflow.run(
  # Path of the folder containing the MLflow project: output artifact is raw_data.csv
  uri="download_data",
  entry_point="main",
  parameters={
    "file_url": "https://...",
    "output_artifact": "raw_data.csv"
  }
)
#Calls the second component(remove_duplicates): use output from first component (raw_data.csv) as input
#Here since we use Weights&Bias as artifact store, we can use "raw_data.csv:latest" to use the latest version of the output artifact from first component
mlflow.run(
  uri="remove_duplicates",
  entry_point="main",
  parameters={
    "input_artifact": "raw_data.csv:latest",
    "output_artifact": "clean_data.csv"
  }
)