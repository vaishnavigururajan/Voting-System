from django.db import models
from django.contrib.auth.models import User

class Election(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    election = models.ForeignKey(Election, related_name='candidates', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    election = models.ForeignKey(Election, related_name='votes', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'election')
