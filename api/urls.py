from django.urls import path
from . import views

urlpatterns =[
    path("register.html",views.register),
    path("login.html",views.login),
    path("dashboard.html",views.dashboard),
    path("lesson/",views.lesson),
    path("open/link/",views.lesson_check),
    path("history/",views.history),
    path("futere/lessons/",views.unstarted_lesson)
]