from flask import Blueprint, jsonify, request
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.app import db
from flask_jwt_extended import jwt_required

episode_bp = Blueprint('episode_bp', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([
        {"id": ep.id, "date": ep.date, "number": ep.number}
        for ep in episodes
    ])

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return {"error": "Episode not found"}, 404

    appearances = [
        {
            "id": a.id,
            "rating": a.rating,
            "guest": {
                "id": a.guest.id,
                "name": a.guest.name,
                "occupation": a.guest.occupation
            }
        } for a in episode.appearances
    ]

    return {
        "id": episode.id,
        "date": episode.date,
        "number": episode.number,
        "appearances": appearances
    }

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return {"error": "Episode not found"}, 404

    db.session.delete(episode)
    db.session.commit()
    return {"message": "Episode deleted"}, 200
