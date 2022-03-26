from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.http import HttpResponse
from bug_tracker.models import BugTracker


class IndexListView(ListView):
    """ View will display all Bug Tracker objects in a list on the hompage

    """
    model = BugTracker


class BugCreateView(CreateView):
    """View will give user ability to create new bug object

    """
    model = BugTracker
    fields = ["bug_title", 'project_name', 'date_occured',
              'bug_description', 'bug_risk']
