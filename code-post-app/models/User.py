from django.db import models
import bcrypt
from django.core.exceptions import ValidationError

salt = bcrypt.gensalt()

# functions for using bcrypt to encrypt passwords
def validate_password(self, key, password):
    if len(password) > 7:
        return bcrypt.hashpw(password.encode('utf-8'), salt)
    else:
        raise ValidationError('Your password must be at least 8 characters.')

def verify_password(self, password):
    return bcrypt.checkpw(
        password.encode('utf-8'),
        self.password.encode('utf-8')
    )

class User(models.Model):
    username = models.Charfield(max_length=48, unique=True)
    email_address = models.CharField(max_length=320, unique=True, validators=[validate_email])
    isAdmin = models.BooleanField(default=False)
    password = models.CharField(max_length=64, min_length=8, validators=[validate_password, verify_password])

    class Meta:
        app_label = 'code-post-app'