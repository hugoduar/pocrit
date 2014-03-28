from django.db import models

# Category: kind of thing 
class Category(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=240)

# Thing: thing to be reviewed
class Thing(models.Model):
	name = models.CharField(max_length=140)
	description = models.CharField(max_length=500)
	category = models.ForeignKey(Category)
	dateCreated = models.DateTimeField('date published')

# Review: result of thing 
class Review(models.Model):
	content = models.CharField(max_length=100)
	description = models.CharField(max_length=240)
	thing = models.ForeignKey(Thing)
	dateCreated = models.DateTimeField('date published')

# Critic: person that make review
class Critic(models.Model):
	username = models.CharField(max_length=30)
	email =  models.CharField(max_length=50)
	registered = models.DateTimeField('date published')