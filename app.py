from flask import Flask
from flask_restful import Api, Resource, reqparse
import random

app = Flask(__name__)
api = Api(app)

@app.route('/home')
def loadtesterapp():
    return """<h1>Faker Load Tester App</h1>
    <body>
    <p>You have succesfully loaded the loadtester app. Now try making some calls to your api</p>
    </body>
    """
author_quotes = [
    {"id": 0, "author": "A.W. Tozer", "quote": "Only an evil desire to shine makes us want to appear other than we are."},
    {"id": 1, "author": "G.K. Chesterton", "quote": "Truth, of course, must of necessity be stranger than fiction, for we have made fiction to suit ourselves."},
    {"id": 3, "author": "Upton Sinclair", "quote": "It is difficult to get a man to understand something, when his salary depends on his not understanding it."},
]

class Quote(Resource):

    def get(self, id=0):
        if id == 0:
            return random.choice(author_quotes), 200

            for quote in author_quotes:
                if(quote["id"] == id):
                    return quote, 200
            return "Quote not found", 404

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("quote")
        params = parser.parse_args()

        for quote in author_quotes:
            if(id == quote["id"]):
                return f"Quote with id {id} already exists", 400

        quote = {
            "id": int(id),
            "author": params["author"],
            "quote": params["quote"]
        }

        author_quotes.append(quote)
        return quote, 201

    def put(self, id):
      parser = reqparse.RequestParser()
      parser.add_argument("author")
      parser.add_argument("quote")
      params = parser.parse_args()

      for quote in author_quotes:
          if(id == quote["id"]):
              quote["author"] = params["author"]
              quote["quote"] = params["quote"]
              return quote, 200
      
      quote = {
          "id": id,
          "author": params["author"],
          "quote": params["quote"]
      }
      
      author_quotes.append(quote)
      return quote, 201

    def delete(self, id):
      global author_quotes
      author_quotes = [qoute for qoute in author_quotes if qoute["id"] != id]
      return f"Quote with id {id} is deleted.", 200

api.add_resource(Quote, "/author-quotes", "/author-quotes/", "/author-quotes/<int:id>")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)