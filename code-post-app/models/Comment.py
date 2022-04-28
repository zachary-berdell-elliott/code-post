from django.db import models

class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    snippet_id = models.ForeignKey(Snippet, on_delete=models.CASCADE)
    comment_text = models.TextField()
    added_at = models.DateTimeField(default=datetime.now)

    class Meta:
        app_label ='code-post-app'