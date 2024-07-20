from django.contrib import admin

# Register your models here.
from . models import Election, Candidate, Vote

admin.site.register(Election)
admin.site.register(Candidate)
admin.site.register(Vote)