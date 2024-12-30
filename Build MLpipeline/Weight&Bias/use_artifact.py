#!/usr/bin/env python
import argparse
import logging
import pathlib
import wandb

"""
python use_artifact.py --artifact_name zhiconghuang-non/exercise_1/zen_of_python:v1
"""
logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    logger.info("Creating run in project exercise_1")
    #Set up a run at the sepcifief project
    run = wandb.init(project="exercise_1", job_type="use_file")

    logger.info("Getting artifact")
    #Pick an artifact to use 
    artifact = run.use_artifact(args.artifact_name, type='text_file')
    #Download this artifact at a local location
    filepath = artifact.download()

    logger.info("Artifact content:")
    print(f"Artifact is downloaded at {filepath}")
    # with open(filepath, "r") as fp:
    #     content = fp.read()

    # print(content)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
        description="Use an artifact from W&B", fromfile_prefix_chars="@"
    )

    parser.add_argument(
        "--artifact_name", type=str, help="Name and version of W&B artifact", required=True
    )

    args = parser.parse_args()

    go(args)