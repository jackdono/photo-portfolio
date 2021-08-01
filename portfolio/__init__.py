from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
import stripe

def create_app():
    app=Flask(__name__)
    #app.debug=True
    #app.secret_key='jdsecretkey'

    bootstrap = Bootstrap(app)

    @app.errorhandler(404)
    def page_not_found(e):
        return redirect(url_for('main.home'))

    from . import views
    app.register_blueprint(views.bp)

    return app