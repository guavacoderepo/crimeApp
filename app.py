from flask import Flask, request, jsonify
import json
from flask_cors import CORS
from src import scrape_all, scrape_one
from src.utils.context import context_keywords


def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route("/")
    def index():
        return "<p>Welcome to crime analysis app home page</p>"

    @app.route('/api/v1/scrap/all')
    def scrap_all_pages():
        scrape_all()
        return {"status": True, "msg": "scrapping all pages"}

    @app.route('/api/v1/scrap/single')
    def scrap_one_page():
        scrape_one()
        return {"status": True, "msg": "scrapping one page"}

    @app.route('/api/v1/context/newstext', methods=["POST"])
    def analyse_context():
        try:
            if request.method == "POST":
                #    get the context to analze
                body = request.get_json()
                body = str(body["context"])

                # bodydata = json.dumps()

                for keys, values in context_keywords.items():
                    # loop through each text and get text
                    if keys == "Politics":
                        Politics = len(
                            [keyword for keyword in values if keyword.lower() in body.lower()])
                    if keys == "Legal Matters":
                        Legal = len(
                            [keyword for keyword in values if keyword.lower() in body.lower()])
                    if keys == "Financial/Bank":
                        Financial = len(
                            [keyword for keyword in values if keyword.lower() in body.lower()])
                    if keys == "Protest":
                        Protest = len(
                            [keyword for keyword in values if keyword.lower() in body.lower()])
                    if keys == "Security":
                        Security = len(
                            [keyword for keyword in values if keyword.lower() in body.lower()])
                    if keys == "Pandemic":
                        Pandemic = len(
                            [keyword for keyword in values if keyword.lower() in body.lower()])
                    if keys == "Education":
                        Education = len(
                            [keyword for keyword in values if keyword.lower() in body.lower()])
                    if keys == "Employment":
                        Employment = len(
                            [keyword for keyword in values if keyword.lower() in body.lower()])

                sum = Education+Pandemic+Politics+Legal+Financial+Security+Employment+Protest

                # print(keyword.lower())

                return {
                    "status": True,
                    "value": "%",
                    "data": {
                        "Education": percentage(sum=sum, value=Education),
                        "Pandemic": percentage(sum=sum, value=Pandemic),
                        "Politics": percentage(sum=sum, value=Politics),
                        "Legal": percentage(sum=sum, value=Legal),
                        "Employment": percentage(sum=sum, value=Employment),
                        "Financial": percentage(sum=sum, value=Financial),
                        "Security": percentage(sum=sum, value=Security),
                        "Protest": percentage(sum=sum, value=Protest)
                    }
                }

            else:

                return {"status": False, "msg": "get not allow on this route.."}

        except Exception as e:
            return {"status": False, "msg": str(e)}

    return app


def percentage(sum, value):
    per = (value/sum)*100

    return per


app = create_app()

if __name__ == "__main__":
    runApp = app
    runApp.run(debug=True)
