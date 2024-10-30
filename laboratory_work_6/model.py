""" Model """

# pylint: disable=E1101

from dataclasses import dataclass

import tensorflow as tf


@dataclass
class Model:
    """Model"""

    def __init__(self, data):
        """Init"""

        self.subsequence = tf.keras.Sequential(
            [
                tf.keras.layers.Input(shape=(data.shape[1], 1)),
                tf.keras.layers.LSTM(64, return_sequences=True),
                tf.keras.layers.LSTM(32),
                tf.keras.layers.Dense(1),
            ]
        )

        self.subsequence.compile(loss="mean_squared_error", optimizer="adam")

    def training(self, seq1, seq2, epochs):
        """training"""

        self.subsequence.fit(seq1, seq2, epochs=epochs, batch_size=32)

    def predictions(self, data):
        """predictions"""

        return self.subsequence.predict(data)
