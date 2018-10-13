from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np
from text_step_model import cl
app = Flask(__name__)
api = Api(app)
# create new model object
model = cl
# load trained classifier
clf_path = '/Users/EricZhong/mhacks_project/text_to_step.pkl'
with open(clf_path, 'rb') as f:
    model.clf = pickle.load(f)
# # load trained vectorizer
# vec_path = 'lib/models/TFIDFVectorizer.pkl'
# with open(vec_path, 'rb') as f:
#     model.vectorizer = pickle.load(f)

parser = reqparse.RequestParser()
parser.add_argument('query')

class PredictStep(Resource):
    def get(self):
        # use parser and find the user's query
        args = parser.parse_args()
        user_query = args['query']
        # vectorize the user's query and make a prediction
        # uq_vectorized = model.vectorizer_transform(
        #     np.array([user_query]))
        prediction = model.classify(user_query)
        pred_proba = model.prob_classify(user_query)
        # Output 'Negative' or 'Positive' along with the score
        pred_text = prediction

        # round the predict proba value and set to new variable
        confidence = str(pred_proba.prob(pred_proba.max()))
        # create JSON object
        output = {'prediction': pred_text, 'confidence': confidence}

        return output


api.add_resource(PredictStep, '/')

# example of another endpoint
# api.add_resource(PredictRatings, '/ratings')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
