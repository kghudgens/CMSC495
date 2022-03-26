from django.forms import ModelForm, SelectDateWidget
from bug_tracker.models import BugTracker


class BugTrackerForm(ModelForm):
    class Meta:
        model = BugTracker
        fields = ["bug_title", 'project_name', 'date_occured',
                  'bug_description', 'bug_risk']
        labels = {
            'bug_title': ("Exception Title"),
            'project_name': ("Project"),
            'date_occured': ("Bug Found"),
            'bug_description': ("Describe the Bug"),
            'but_risk': ("Risk Level")

        }
        widgets = {
            'date_occured': SelectDateWidget()
        }
