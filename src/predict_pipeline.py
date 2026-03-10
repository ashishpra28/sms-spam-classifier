import pickle

class PredictPipeline:

    def __init__(self):
        self.model = pickle.load(open("model/model.pkl","rb"))

    def predict(self,message):

        prediction = self.model.predict([message])[0]

        return prediction