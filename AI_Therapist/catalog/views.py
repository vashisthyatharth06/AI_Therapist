# views.py
from django.shortcuts import render, redirect
from catalog.forms import RegisterForm
from catalog.forms import SelectMoodForm
from catalog.models import Doctor ,Calendar
from django.views import generic
import datetime
from django.contrib.auth.models import User
# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

            return redirect("/catalog")
    else:
        form = RegisterForm()

    return render(response, "register.html", {"form":form})
def index(response):
	return render(response,"index.html")
def about(response):
	return render(response,"about.html")
def chat(request):
   
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = SelectMoodForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
        	

            select_mood=form.cleaned_data['today_mood']
            record=Calendar()
            record.mood=select_mood
            record.mood_date=datetime.datetime.today()
            
            record.yachak=request.user
            record.save()
            
        return render(request, 'chat.html', {'form':form,'select_mood':select_mood,'flag':1})
    else:
        form=SelectMoodForm()
        return render(request, 'chat.html', {'form':form,'flag':0})
class DoctorListView(generic.ListView):
    model = Doctor  
    paginate_by = 10 
class DoctorDetailView(generic.DetailView):
    model = Doctor
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
class CalendarListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = Calendar
    template_name ='catalog/my_moods.html'
    
    
    def get_queryset(self):
        return Calendar.objects.filter(yachak=self.request.user)
    


