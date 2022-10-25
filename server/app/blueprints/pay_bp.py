from decimal import Decimal
import json
from flask import Blueprint, jsonify, render_template, request
from app import lnbits
from app.forms import pay_form

pay_bp = Blueprint("pay_bp", __name__)


@pay_bp.route("", methods=["GET"])
@pay_bp.route("/", methods=["GET"])
def get():
    print(__name__, "get")
    amount = Decimal(request.args.get("amount", 3000))
    memo = str(request.args.get("memo", ""))
    data = {
        "amount": "",
        "reference": "",
        "address": "",
    }
    return render_template("pay.html", data=data), 200
