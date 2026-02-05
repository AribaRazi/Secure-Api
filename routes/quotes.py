from flask import Blueprint, request, jsonify
from redis_client import r
from db import get_db
from flask_jwt_extended import jwt_required, get_jwt_identity

quotes_bp = Blueprint("quotes", __name__)

@quotes_bp.route("/quotes")
@jwt_required()
def get_quotes():
    
    user_email = get_jwt_identity()

    cache_key = f"quotes:{user_email}"

    cached = r.get(cache_key)
    if cached:
        return jsonify({
            "source": "redis_cache",
            "data": eval(cached)
        })

    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM quotes")
    quotes = cursor.fetchall()

    r.setex(cache_key, 180, str(quotes))

    return jsonify({
        "source": "mysql_db",
        "data": quotes
    })
