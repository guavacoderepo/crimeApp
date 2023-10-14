from flask import Flask, request
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

                for key, values in context_keywords.items():
                    # loop through each text and get text
                    for keyword in values:
                        print(keyword)
                        if keyword in body:
                            print(keyword)

                    # print(key)
                    # print("data my oh data")

                return {"status": True, "data": body["context"]}

            else:

                return {"status": False, "msg": "get not allow on this route.."}

        except Exception as e:
            return {"status": False, "msg": e}

    return app


app = create_app()

if __name__ == "__main__":
    runApp = app
    runApp.run(debug=True)
