from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def index(request : HttpRequest):
    return render(request,"app/index.html")

# Has a form that allows a user to create a new activity
# When the form is submitted they are redirected to the /activity/<id> 
# page for the new activity that was just created
def new_activity(request : HttpRequest):
    return render(request,"app/new_activity.html")

#Displays the name of the Activity
# Displays a list of all of the TimeLogs for the Activity
# Displays a link to the /activity/<id>/new_timelog page
def activity(request : HttpRequest, id : int):
    return render(request,"app/activity.html")


#Displays the title of the activity
#Displays a form that the users can submit to create a new TimeLog
# Use an <input type="datetime-local"> as the inputs for the start and end times.
# When the form is submitted, redirect to the /activity/<id> page
def new_timelog(request : HttpRequest ,id:int):
    return render(request,"app/new_timelog.html")