import pickle
from pathlib import Path

# Using the Path object, create a `project_root` variable
# set to the absolute path for the root of this project directory
#### YOUR CODE HERE
 
# Using the `project_root` variable
# create a `model_path` variable
# that points to the file `model.pkl`
# inside the assets directory
#### YOUR CODE HERE

from pathlib import Path
import pickle

# Path to root of the project
ROOT_DIR = Path(__file__).resolve().parents[1]

# Path to model.pkl file
MODEL_PATH = ROOT_DIR / "models" / "model.pkl"

def load_model():
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)
