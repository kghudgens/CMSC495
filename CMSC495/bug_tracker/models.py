from django.db import models

# List of choices the user can select from
risk_list = {"High", "Medium", "Low"}


class BugTracker(models.Model):

    """ 
    Model class represents the bug tracker object. Detailing what problem what the developer is dealing with in their program
    """

    bug_title = models.CharField()
    # what project does the bug belong to
    project_name = models.CharField()
    # when was the bug first noticed
    date_occured = models.DateField()
    bug_description = models.TextField()
    # when was the entry recorded by the user
    date = models.DateTimeField()
    # how important is solving this bug
    bug_risk = models.TextChoices(risk_list)

    def __str__(self):
        """The model will be given the bug's name in the admin panel
        """
        return self.bug_title

    class Meta:
        ordering = ["-date"]
