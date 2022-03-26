from pyexpat import model
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.http import HttpResponse
from bug_tracker.models import BugTracker


class IndexListView(ListView):
    """ View will display all Bug Tracker objects in a list on the hompage. """

    model = BugTracker


class BugCreateView(CreateView):
    """ View will give user ability to create new Bug Tracker objects. """

    model = BugTracker
    fields = ["bug_title", 'project_name', 'date_occured',
              'bug_description', 'bug_risk']


class BugDetailView(DetailView):
    """ View will display the Bug Tracker object in its entirety. """

    model = BugTracker
    context_object_name = 'bug'


class BugUpdateView(UpdateView):
    """View will display a form so the user can update the bug tracker object. """

    model = BugTracker
    fields = ["bug_title", 'project_name', 'date_occured',
              'bug_description', 'bug_risk']
