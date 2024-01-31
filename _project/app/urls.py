from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("new_activity/", views.new_activity, name="new_activity"),  # Add trailing slash
    path("activity/<int:id>",views.activity,name="activity"),
    path("activity/new_timelog/<int:id>",views.new_timelog,name="new_timelog"),
]