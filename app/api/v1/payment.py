#! /usr/bin/env python3.6

import os
from flask import Flask, Blueprint, redirect, request


payment = Blueprint('payment', __name__)



@payment.route('/checkout/<float:price>')
def paypal_checkout(price):
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "transactions": [{
            "amount": {
                "total": str(price),
                "currency": "USD"
            },
            "description": "Purchase description"
        }],
        "redirect_urls": {
            "return_url": url_for('views.paypal_success', _external=True),
            "cancel_url": url_for('views.paypal_cancel', _external=True)
        }
    })

    if payment.create():
        #print("Created")
        approval_url = next(link.href for link in payment.links if link.rel == "approval_url")
        return redirect(approval_url)
    else:
        return "Payment creation failed"

@payment.route('/success')
def paypal_success():
    return "Payment successful! Thank you."

@payment.route('/cancelled')
def paypal_cancel():
    return "Payment cancelled. Please try again."