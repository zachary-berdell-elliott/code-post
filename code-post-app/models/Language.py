from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, required=False)

    class Meta:
        app_label = 'code-post-app'