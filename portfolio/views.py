from flask import Blueprint, render_template, request, redirect, url_for, jsonify
import stripe

bp = Blueprint('main', __name__)

stripe_keys = {
    'public_key':   'pk_test_51IOBlrCsapAQXjSXOSE1pYcYBHuheqGItrYEs5Yp6gncmAjKFqXACPwAZhZG8vuP95VPbSm8sG8GdOxjzkECqqGN00l95OxdlV',
    'secret_key':   'sk_test_51IOBlrCsapAQXjSXTDLTKDQB0OGuR9joYuKhu1CadlpOBaz7gDKXi8ZaYRedV6Fv4GrKb5ECuaJo0XQyceOqTu7t00Gz5Ppe8F',
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