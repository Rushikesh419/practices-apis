
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('movieapi/',views.LCMovieAPI.as_view()),
    #path('movieapi/',views.MovieCreate.as_view()),
    #path('movieapi/<int:pk>',views.MovieRetrive.as_view()),
    #path('movieapi/<int:pk>',views.MovieUpdate.as_view()),
    path('movieapi/<int:pk>',views.RUDSovieAPI.as_view()),
    
]
