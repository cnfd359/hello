import numpy as np


class LogLoss():
    def __init__(self):
        pass


    def train(self, X, y):
        self.X_train = X
        self.y_train = y
        w = np.random.normal(size=(X.shape[1],1))

        while True:
            fsfsdfsfsg