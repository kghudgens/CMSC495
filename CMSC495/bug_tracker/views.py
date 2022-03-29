from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.http import HttpResponse
from bug_tracker.forms import BugTrackerForm
from bug_tracker.models import BugTracker


def about(request):
    return render(request, 'bug_tracker/about.html')


class IndexListView(ListView):
    """ View will display all Bug Tracker objects in a list on the hompage. """

    model = BugTracker


class BugCreateView(CreateView):
    """ View will give user ability to create new Bug Tracker objects. """

    model = BugTracker
    form_class = BugTrackerForm
    # on successful submission of form, the view will send the user to the list view index
    success_url = reverse_lazy('index_list')

    def form_valid(self, form_class):
        """ Method validates the form and assigns it to the user signed in"""
        form_class.instance.user = self.request.user
        return super().form_valid(form_class)


class BugDetailView(DetailView):
    """ View will display the Bug Tracker object in its entirety. """

    model = BugTracker
    context_object_name = 'bug'


class BugUpdateView(UpdateView):
    """View will display a form so the user can update the bug tracker object. """

    model = BugTracker
    fields = ["bug_title", 'project_name', 'date_occured',
              'bug_description', 'bug_risk']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy("index_list")


class BugDeleteView(DeleteView):

    model = BugTracker
    success_url = reverse_lazy('index_list')
