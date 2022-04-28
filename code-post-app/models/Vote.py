from django.db import models

class Vote(models.Model):
    upvotes = models.BooleanField(default=False)
    downvotes = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    snippet_id = models.ForeignKey(Snippet, on_delete=models.CASCADE)

    class Meta:
        app_label = 'code-post-app'