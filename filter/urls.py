from django.urls import path,include
from . import views
urlpatterns =[
    path('filter/',views.FilterPostAPIView.as_view()),
    path('filter/<str:email>',views.FilterPostAPIView.as_view())
 ]