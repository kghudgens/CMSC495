""" Module is used to register all models with the Django Admin Site"""
from django.contrib import admin
from bug_tracker.models import BugTracker

admin.site.register(BugTracker)
