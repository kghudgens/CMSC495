from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from bug_tracker.models import BugTracker


class IndexListView(ListView):
    """ View will display all Bug Tracker objects in a list on the hompage

    Args:
        ListView (_type_): View that displays all objects as list at the users discretion
    """
    model = BugTracker
