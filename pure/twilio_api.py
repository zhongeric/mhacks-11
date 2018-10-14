from flask import Flask
from twilio.rest import Client
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np
from text_step_model import cl
app = Flask(__name__)
api = Api(app)
# create new model object
model = cl
# load trained classifier
clf_path = 'home/ezhong1900/new_mhacks/text_to_step.pkl'
with open(clf_path, 'rb') as f:
    model.clf = pickle.load(f)

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACcc3e85148706449da8e73f93cd26ece2'
auth_token = 'df02a06ee966b53fbe423bb0d815143d'
client = Client(account_sid, auth_token)
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

newparser = reqparse.RequestParser()
newparser.add_argument('body')
newparser.add_argument('destination')
class ActivateTwilio(Resource):
    def get(self):
        args = newparser.parse_args()
        print(args)
        message_body = args['body']
        destination = args['destination']
        message = client.messages \
            .create(
                 body=message_body,
                 to =destination,
                 from_='+15862819961'
             )
        print(message.sid)

api.add_resource(PredictStep, '/')
api.add_resource(ActivateTwilio, '/twilio')

# example of another endpoint
# api.add_resource(PredictRatings, '/ratings')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
