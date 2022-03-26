from django.urls import path

from bug_tracker.views import IndexListView, BugCreateView

urlpatterns = [
    # Home page
    path('', IndexListView.as_view(), name='index_list'),
    path('create/', BugCreateView.as_view(), name='create_bug')
]
