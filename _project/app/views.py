from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import Activity,TimeLog

# Create your views here.
def index(request : HttpRequest):
    activities = Activity.objects.all()
    return render(request,"app/index.html",{"activities":activities})

# Has a form that allows a user to create a new activity
# When the form is submitted they are redirected to the /activity/<id> 
# page for the new activity that was just created
def new_activity(request : HttpRequest):
    params = request.POST
    if "activity_name" in params:
        activity_name = params["activity_name"]
        activity = Activity(name=activity_name)
        activity.save()
        return redirect('index')  # Redirect to the 'index' page
    return render(request, "app/new_activity.html")

#Displays the name of the Activity
# Displays a list of all of the TimeLogs for the Activity
# Displays a link to the /activity/<id>/new_timelog page
def activity(request : HttpRequest, id : int):
    activity = Activity.objects.get(pk=id)
    timelogs = TimeLog.objects.filter(activity=activity)
    data = {"activity":activity,"timelogs":timelogs}
    return render(request,"app/activity.html",{"data":data})


#Displays the title of the activity
#Displays a form that the users can submit to create a new TimeLog
# Use an <input type="datetime-local"> as the inputs for the start and end times.
# When the form is submitted, redirect to the /activity/<id> page
def new_timelog(request : HttpRequest ,id:int):
    activity = Activity.objects.get(pk=id)
    params = request.POST
    if params and "start_time" in params and "end_time" in params:
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        if start_time and end_time:
            timelog = TimeLog(start_time=start_time,end_time=end_time,activity=activity)
            timelog.save()
            return redirect('activity',id=id)
    return render(request,"app/new_timelog.html", {"activity":activity})