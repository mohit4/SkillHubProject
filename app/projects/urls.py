from django.urls import path

from .views import (
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
)

app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='all-projects-list'),
    path('create/', ProjectCreateView.as_view(), name='project-create'),
    path('<pk>/', ProjectDetailView.as_view(), name='project-details'),
    path('<pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('<pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
]
