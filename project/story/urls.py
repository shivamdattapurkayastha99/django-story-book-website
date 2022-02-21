
from django.urls import path
from story import views
app_name="story"
urlpatterns = [
    
    path('',views.home,name='home'),
]