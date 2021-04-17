from django.db import models
# Create your models here.
from datetime import datetime

#other field restriction is applied in sql
class Song(models.Model):
	ID = models.IntegerField()
	name_of_the_song = models.CharField(max_length=100)
	duration = models.IntegerField()
	uploaded_time = models.DateTimeField()
	class Meta:
		managed = False
		db_table = 'song'

class Podcast(models.Model):
	ID = models.IntegerField()
	name_of_the_song = models.CharField(max_length=100)
	duration = models.IntegerField()
	uploaded_time = models.DateTimeField()
	host = models.CharField(max_length=100)
	participants = models.CharField(max_length=100)
	class Meta:
		managed = False
		db_table = 'podcast'


class Audiobook(models.Model):
	ID = models.IntegerField()
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	narrator = models.CharField(max_length=100)
	duration = models.IntegerField()
	uploaded_time = models.DateTimeField()
	class Meta:
		managed = False
		db_table = 'audiobook'
