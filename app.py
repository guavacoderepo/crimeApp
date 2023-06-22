from flask import Flask
from src.sahara import scrape


def create_app():
    app = Flask(__name__)
    
    return app


if __name__ == "__main__":
    runApp = create_app()
    runApp.run()
