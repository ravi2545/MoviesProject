import src.controllers.api as flask_app
import os

app = flask_app.create_app()

if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)
