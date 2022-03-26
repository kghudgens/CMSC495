from django.urls import path

from bug_tracker.views import IndexListView

urlpatterns = [
    # Home page
    path('', IndexListView.as_view(), name='index_list'),
]
