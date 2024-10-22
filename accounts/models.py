import mongoengine as me
from mongoengine import Document, StringField, EmailField
from django.contrib.auth.hashers import check_password


class UserDetails(Document):
   username = StringField(required=True, unique=True)
   email = StringField(required=True, unique=True)
   password = StringField(required=True)
   created_at = DateTimeField(default=datetime.utcnow)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
