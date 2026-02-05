from flask import Blueprint, request, jsonify
from redis_client import r
import random
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/send-otp", methods=["POST"])
def send_otp():
    email = request.json["email"]

    limit_key = f"otp_limit:{email}"

    count = r.get(limit_key)

    if count and int(count) >= 3:
        return jsonify({
            "message": "Too many OTP requests. Try again after 1 minute."
        }), 429

    if not count:
        r.setex(limit_key, 60, 1)
    else:
        r.incr(limit_key)

    otp = str(random.randint(100000, 999999))
    
    r.setex(email, 120, otp)

    return jsonify({
        "message": "OTP sent",
        "otp": otp
    })


@auth_bp.route("/verify-otp", methods=["POST"])
def verify_otp():
    email = request.json["email"]
    user_otp = request.json["otp"]

    saved_otp = r.get(email)

    if not saved_otp:
        return jsonify({"message": "OTP expired or not found"})

    if saved_otp == user_otp:
        r.delete(email)

        token = create_access_token(identity=email)

        return jsonify({
        "message": "OTP verified successfully",
        "token": token
    })
        
    return jsonify({"message": "Invalid OTP"})
