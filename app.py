from flask import Flask
from flask_cors import CORS
from src import scrape_all, scrape_one


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

    return app


if __name__ == "__main__":
    runApp = create_app()
    runApp.run()
