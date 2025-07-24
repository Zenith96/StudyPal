from . import views
from django.urls import path

urlpatterns = [
    path('',views.DashBoardView,name ="view-dashboard"),
    path('tasks/',views.TaskView.as_view(),name ="view-tasks"),
    path('notes/',views.NotesView.as_view(),name ="view-notes")
]