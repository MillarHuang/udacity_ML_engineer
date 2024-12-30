"""
Bash: pytest Data_validation/ -vv 
Data_visualization/: directory
-vv:means verbose, will have better visualization of the result
"""
import pytest
import wandb
import pandas as pd

run = wandb.init()

@pytest.fixture(scope="session")
def data():

    local_path = run.use_artifact("exercise_5/preprocessed_data.csv:latest").file()
    df = pd.read_csv(local_path, low_memory=False)

    return df


def test_data_length(data):
    """
    We test that we have enough data to continue
    """
    assert len(data) > 1000
    

def test_number_of_columns(data):
    """
    We test that we have enough data to continue
    """
    assert data.shape[1] == 19


#When the fixture got modified, the modification will persist for all subsequent tests that use that fixture
@pytest.fixture(scope="session")
def session_fixture():
    data = {"value": 0}
    return data

def test_one(session_fixture):
    # Modify the fixture
    session_fixture["value"] += 1
    assert session_fixture["value"] == 1

def test_two(session_fixture):
    # Test sees the modified fixture
    assert session_fixture["value"] == 1

