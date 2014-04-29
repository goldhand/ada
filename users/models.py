# -*- coding: utf-8 -*-

# Import the basic Django ORM models library
from django.db import models

from django.utils.translation import ugettext_lazy as _


# Subclass AbstractUser
class UserProfile(models.Model):

	TYPE_CHOICES = (
		("Voting", "Voting"),
		("Caucus", "Caucus"),
		("Association", "Association")
		)

	user = models.OneToOneField("auth.User")
	dispensary = models.CharField(max_length=255, blank=True)
	phone = models.CharField(max_length=20, blank=True)
	type = models.CharField(max_length=255, choices=TYPE_CHOICES, default="Voting")
	bio = models.TextField(blank=True)

	def __unicode__(self):
		return self.user.username