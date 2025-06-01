import pandas as pd
import numpy as np

Xs = ["x" + str(i) for i in range(1, 22)]
Ys = ["y" + str(i) for i in range(1, 22)]
mycols = [item for i in range(1, 22) for item in (f"x{i}", f"y{i}")]

def transform_record(record):
    # Translate
    record[Xs] -= record[Xs[0]]
    record[Ys] -= record[Ys[0]]

    # Scale
    record[Xs] /= (max(record[Xs]) - min(record[Xs]))
    record[Ys] /= (max(record[Ys]) - min(record[Ys]))

    # Rotate
    theta = np.arctan2(record[Xs[9]], record[Ys[9]])
    cos = np.cos(theta)
    sin = np.sin(theta)
    R = np.array([[cos, -sin], [sin, cos]])
    rotated = R @ np.vstack((record[Xs], record[Ys]))
    record[Xs], record[Ys] = rotated[0], rotated[1]

    # Flip sign of Xs
    record[Xs] = np.sign(record[Xs[5]] - record[Xs[9]]) * record[Xs]

    return record

def preprocess(flat_landmarks):
    record = pd.DataFrame([flat_landmarks], columns=mycols)
    processed = record.apply(transform_record, axis=1)
    return processed
