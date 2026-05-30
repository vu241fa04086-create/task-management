from flask import Blueprint
from flask import request
from flask import jsonify
from flask import render_template

from middleware.jwt_middleware import token_required

from services.payment_service import (
    create_order_service,
    save_payment_service
)

payment_bp = Blueprint(
    "payment_bp",
    __name__
)


@payment_bp.route("/")
def payment_ui():

    return render_template(
        "payment.html"
    )


@payment_bp.route("/create-order", methods=["POST"])
@token_required
def create_order():

    data = request.json

    order = create_order_service(
        data["amount"]
    )

    return jsonify(order)


@payment_bp.route("/save-payment", methods=["POST"])
@token_required
def save_payment():

    response = save_payment_service(
        request.json,
        request.user_id
    )

    return jsonify(response)