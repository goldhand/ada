# -*- coding: utf-8 -*-

# Import the basic Django ORM models library
from django.db import models

from django.utils.translation import ugettext_lazy as _


# Subclass AbstractUser
class UserProfile(models.Model):

	user = models.OneToOneField("auth.User")
	bio = models.TextField(blank=True)

	def __unicode__(self):
		return self.user.username