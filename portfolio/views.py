from flask import Blueprint, render_template, request, redirect, url_for, jsonify
import stripe

bp = Blueprint('main', __name__)

stripe_keys = {
    'public_key':   'public key goes here',
    'secret_key':   'secret key goes here',
}

stripe.api_key = stripe_keys["secret_key"]


@bp.route('/')
def home():
    return render_template('comingsoon.html')

@bp.route('/zine')
def zine():
    return render_template('zine.html')

@bp.route('/success')
def success():
    return render_template('comingsoon.html')