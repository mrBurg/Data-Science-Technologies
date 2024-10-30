"""Laboratory work 6"""

# pylint: disable=E0401

from pathlib import Path

import numpy as np

from utils import Utils
from model import Model
from rendering import Rendering as Render


if __name__ == "__main__":
    FILE_PATH = Path(__file__).parent.joinpath("./").resolve()
    FILE_NAME = "user_behavior_dataset.xls"
    COLUMBS = ["App Usage Time (min/day)"]
    LEAR_COEF = 0.6
    EPOCHS = 10
    SEQ_SIZE = 100

    utils = Utils()
    render = Render()

    file_data = utils.read_excel(FILE_PATH, FILE_NAME, usecols=COLUMBS)
    data = file_data.values

    train_num = int(len(data) * LEAR_COEF)
    train_data = data[:train_num]
    test_data = data[train_num:]

    seq1_train, seq2_train = utils.create_sequence(train_data, SEQ_SIZE)
    seq1_test, seq2_test = utils.create_sequence(test_data, SEQ_SIZE)

    model = Model(seq1_train)

    model.training(seq1_train, seq2_train, EPOCHS)
    predictions = model.predictions(seq1_test)

    mse = np.sqrt(np.mean((seq2_test - predictions) ** 2))
    print("Оцінка моделі (MSE):", mse)

    labels = ["Дані", "Передбачення"]
    render.show(
        seq2_test,
        predictions,
        title="Графік: " + " + ".join(labels),
        labels=labels,
    )
