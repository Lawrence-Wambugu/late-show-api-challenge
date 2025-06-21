from flask import Blueprint, request, jsonify
from server.models.appearance import Appearance
from server.models.guest import Guest
from server.models.episode import Episode
from server.app import db
from flask_jwt_extended import jwt_required

appearance_bp = Blueprint('appearance_bp', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()

    try:
        rating = int(data.get("rating"))
        if not (1 <= rating <= 5):
            raise ValueError
    except:
        return {"error": "Rating must be between 1 and 5"}, 400

    guest = Guest.query.get(data.get("guest_id"))
    episode = Episode.query.get(data.get("episode_id"))

    if not guest or not episode:
        return {"error": "Invalid guest or episode"}, 400

    appearance = Appearance(
        rating=rating,
        guest_id=guest.id,
        episode_id=episode.id
    )
    db.session.add(appearance)
    db.session.commit()

    return jsonify({
        "id": appearance.id,
        "rating": appearance.rating,
        "guest_id": appearance.guest_id,
        "episode_id": appearance.episode_id
    }), 201
