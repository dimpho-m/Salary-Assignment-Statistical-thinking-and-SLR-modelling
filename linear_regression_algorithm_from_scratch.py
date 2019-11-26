import numpy as np 

class LinearRegression:
    def __init__(self):
        self.a = None
        self.b = None
        
    def fit(self, X, y):
        ''' This method takes in the x and y values and uses them to fit a line for the given dataset '''
        
        X = np.ndarray(X)
        y = np.ndarray(y)
        
        self.b = (X -X.mean()) * (y - y.mean()).sum() / ((X -X.mean()) ** 2).sum()
        self.a = y.mean() - self.b * X.mean()

        return self

    def predict(self, X):
        
        X = np.array(X)

        y = self.a + (self.b) * X

        return y