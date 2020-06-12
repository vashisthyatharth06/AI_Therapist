from django.urls import path
from . import views

urlpatterns = [
 path('register/', views.register, name='register'),
 path('', views.index, name='index'),
 path('chat/',views.chat,name='chat'),
 path('about/',views.about,name='about'),
 path('doctor/<int:pk>', views.DoctorDetailView.as_view(), name='doctor-detail'),
 path('doctors/', views.DoctorListView.as_view(), name='doctors'),
 path('user_calendar/', views.CalendarListView.as_view(), name='user_moods'),
]