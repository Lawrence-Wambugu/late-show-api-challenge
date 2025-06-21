from server.app import create_app, db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

app = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()

    u = User(username="testuser")
    u.set_password("password")

    g1 = Guest(name="Beyoncé", occupation="Singer")
    g2 = Guest(name="Trevor Noah", occupation="Comedian")

    e1 = Episode(date="2024-01-01", number=1)
    e2 = Episode(date="2024-01-02", number=2)

    a1 = Appearance(rating=5, guest=g1, episode=e1)
    a2 = Appearance(rating=4, guest=g2, episode=e2)

    db.session.add_all([u, g1, g2, e1, e2, a1, a2])
    db.session.commit()
