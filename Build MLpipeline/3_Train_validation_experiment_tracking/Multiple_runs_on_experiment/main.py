"""
mlflow run . \
  -P hydra_options="-m random_forest_pipeline.random_forest.max_depth=1,5,10"
mlflow run . \
  -P hydra_options="-m random_forest_pipeline.random_forest.max_depth=range(10,50,3) random_forest_pipeline.tfidf.max_features=range(50,200,50) hydra/launcher=joblib"
"""
import json
import mlflow
import os
import hydra
from omegaconf import DictConfig, OmegaConf


# This automatically reads in the configuration
@hydra.main(config_path='.', config_name='config')
def go(config: DictConfig):

    # Setup the wandb experiment. All runs will be grouped under this name
    os.environ["WANDB_PROJECT"] = config["main"]["project_name"]
    os.environ["WANDB_RUN_GROUP"] = config["main"]["experiment_name"]

    # You can get the path at the root of the MLflow project with this:
    root_path = hydra.utils.get_original_cwd()

    # Serialize decision tree configuration
    model_config = os.path.abspath("random_forest_config.yml")

    with open(model_config, "w+") as fp:
        fp.write(OmegaConf.to_yaml(config["random_forest_pipeline"]))

    _ = mlflow.run(
        os.path.join(root_path, "random_forest"),
        "main",
        parameters={
            "train_data": config["data"]["train_data"],
            "model_config": model_config
        },
    )


if __name__ == "__main__":
    go()
