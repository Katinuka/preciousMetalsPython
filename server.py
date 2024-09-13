from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def create_app():
    # Import and register routes inside function
    from registration import registration_bp
    from login import login_bp
    from homepages import homepages_bp

    app.register_blueprint(registration_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(homepages_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=8000, debug=True)
