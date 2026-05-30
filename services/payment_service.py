import razorpay
from flask import current_app
from models.payment import Payment
from config.database import db


client = razorpay.Client(
    auth=(
        "RAZORPAY_KEY_ID",
        "RAZORPAY_SECRET"
    )
)


def create_order_service(amount):

    order = client.order.create({
        "amount": amount * 100,
        "currency": "INR",
        "payment_capture": 1
    })

    return order


def save_payment_service(data, user_id):

    payment = Payment(
        razorpay_payment_id=data["razorpay_payment_id"],
        amount=data["amount"],
        status="success",
        user_id=user_id
    )

    db.session.add(payment)
    db.session.commit()

    return {
        "message": "Payment saved"
    }