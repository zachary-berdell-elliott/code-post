from django.db import models

class Language(models.Model):
    title = models.CharField(max_length=128)
    attached_code = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=datetime.now)

    class Meta:
        app_label = 'code-post-app'