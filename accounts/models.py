import mongoengine as me
from mongoengine import Document, StringField, EmailField
from django.contrib.auth.hashers import check_password


class UserDetails(Document):
    username = StringField(required=True, unique=True, max_length=150)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
