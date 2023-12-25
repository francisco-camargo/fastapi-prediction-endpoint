import os

import joblib
from sklearn.pipeline import Pipeline

if __name__ == '__main__':
    # Load the model
    model_filename = 'newsgroups_model.joblib'
    model_file = os.path.join(
        os.path.dirname(__file__),
        model_filename,
    )
    loaded_model: tuple[Pipeline, list[str]] = joblib.load(model_file)
    model, targets = loaded_model

    # Run prediction
    inference_input = ['computer cpu memory ram']
    p = model.predict(inference_input)
    print(targets[p[0]])
    print(targets)
