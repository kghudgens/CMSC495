from django.urls import path

from bug_tracker.views import IndexListView, BugCreateView, BugDetailView, BugUpdateView, BugDeleteView

urlpatterns = [
    # Home page
    path('', IndexListView.as_view(), name='index_list'),
    path('create/', BugCreateView.as_view(), name='create_bug'),
    path('<int:pk>/',  BugDetailView.as_view(), name='bug_detail'),
    path('<int:pk>/update/', BugUpdateView.as_view(), name='bug_update'),
    path('<int:pk>/delete', BugDeleteView.as_view(), name='bug_delete')
]
