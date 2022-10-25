import os
import sys

from dotenv import load_dotenv
import waitress

sys.path.append("../")
from app import create_app

load_dotenv()
ENV = os.getenv("ENV")
SERVER_IP = os.getenv("SERVER_IP")
SERVER_PORT = os.getenv("SERVER_PORT")
params = {"host": f"{SERVER_IP}", "port": f"{SERVER_PORT}"}

app = create_app()


def main():
    if ENV == "develop":
        app.run(debug=True, **params)
        # app.run(debug=True, **params, ssl_context="adhoc")
    elif ENV == "master":
        waitress.serve(app, **params)
        # waitress.serve(app, **params, url_scheme="https")

if __name__ == "__main__":
    main()
