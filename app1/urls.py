from django.urls import path
from . import views
urlpatterns = [
    path('',view=views.registation_form,name='registation'),
    path('login/',view=views.login_view,name='login'),
]
