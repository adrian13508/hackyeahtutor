from django.db import models
import uuid
from account.models import CustomUser


# class LearningSession(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)
#     session_id = models.UUIDField(default=uuid.uuid4, editable=False)
#     article_url = models.URLField()
#     start_time = models.DateTimeField(auto_now_add=True)
#     read_status = models.BooleanField(default=False)  # Track if the user has read the article
#     recall_status = models.BooleanField(default=False)  # Track if the recall session has been completed
#     review_status = models.BooleanField(default=False)  # Track if the review step has been completed
#     last_updated = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name
