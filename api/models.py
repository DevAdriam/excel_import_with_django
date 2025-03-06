from django.db import models

class Challenge(models.Model):
    challengeId = models.TextField()
    challengeName = models.TextField()
    challengeDifficulty = models.CharField(max_length=50)

    def __str__(self):
        return self.title

