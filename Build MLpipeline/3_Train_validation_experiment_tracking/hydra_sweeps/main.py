import mlflow
import os
import hydra
from omegaconf import DictConfig
"""
In command line: mlflow run . -P hydra_options="-m parameters.a=3,4,5"
Enable runs to run in parallel: mlflow run . -P hydra_options="hydra/launcher=joblib parameters.a=3,4 parameters.b=range(2,4,1) -m"
"""

# This automatically reads in the configuration
@hydra.main(config_name='config')
def go(config: DictConfig):

    # Setup the wandb experiment. All runs will be grouped under this name
    os.environ["WANDB_PROJECT"] = config["main"]["project_name"]
    os.environ["WANDB_RUN_GROUP"] = config["main"]["experiment_name"]

    # You can get the path at the root of the MLflow project with this:
    root_path = hydra.utils.get_original_cwd()

    _ = mlflow.run(
        os.path.join(root_path, "component"),
        "main",
        parameters={
            "a": config["parameters"]["a"],
            "b": config["parameters"]["b"],
        },
    )


if __name__ == "__main__":
    go()
