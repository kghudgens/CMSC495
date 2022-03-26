from pyexpat import model
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
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


class BugDetailView(DetailView):

    model = BugTracker
    context_object_name = 'bug'


class BugUpdateView(UpdateView):
    model = BugTracker
    fields = ["bug_title", 'project_name', 'date_occured',
              'bug_description', 'bug_risk']
