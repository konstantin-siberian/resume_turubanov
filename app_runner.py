from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return render_template('resume_turubanov.html')

    @app.route("/fancy")
    def hello_world_2():
        return 'Hello world! Fancy!'

    return app








