import mongoengine as me
from mongoengine import Document, StringField, EmailField, DateTimeField
from django.contrib.auth.hashers import check_password
from datetime import datetime

class UserDetails(Document):
    username = StringField(required=True, unique=True)
    email = EmailField(required=True, unique=True)  # Use EmailField for email
    password = StringField(required=True)
    # created_at = DateTimeField(default=datetime.utcnow)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
