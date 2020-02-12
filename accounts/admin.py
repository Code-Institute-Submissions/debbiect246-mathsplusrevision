'''
user profile handler, imports user profile model and 
works with admin to set up a profile for user.
Not fully functional as unable to connect user orders to
profile, despite spending 3 hours talking to tutors and 
some help from slack room.  Future area for development.
'''

from django.contrib import admin

from .models import UserProfile
admin.site.register(UserProfile)
