
from django.urls import path
from story import views
app_name="story"
urlpatterns = [
    
    path('',views.story_list,name='story_list'),
    path('story/<slug:category_slug>',views.story_list,name="story_category"),
    path('<int:id>/',views.story_detail,name='story_detail'),

]