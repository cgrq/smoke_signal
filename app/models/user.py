from datetime import datetime
from .db import db, environment, SCHEMA, add_prefix_for_prod
from .team_memberships import TeamMemberships
from .channel_memberships import ChannelMemberships
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    STATUS = ['online', 'offline', 'away']

    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    profile_image_url = db.Column(db.String(100))
    status = db.Column(db.Enum(*STATUS), name='status')

    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

    # Foreign Keys
    teams = db.relationship(TeamMemberships, back_populates="teams")
    channels = db.relationship(ChannelMemberships, back_populates="channels")
    channels = db.relationship(ChannelMemberships, back_populates="channels")


    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'email': self.email,
            'profile_image_url': self.profile_image_url,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }