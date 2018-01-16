from sklearn import svm
import numpy as np

class MyMLLibrary():

    def __init__(self):
        self.name = "MLLibrary"

    def PerformSVM(self, data, cost):

        X = np.array(data.drop(['patientID','state'], axis=1))
        y = np.array(data['state'])

        model = svm.LinearSVC(C=cost)
        model.fit(X, y)
        predictions = model.predict(X)

        return predictions

if __name__ == '__main__':
    a = MyMLLibrary().PerformSVM()
    print(a)