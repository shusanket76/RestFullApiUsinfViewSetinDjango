from email.mime import base
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path,include

from basyal import views

router = DefaultRouter()
router.register("taskapi", views.TaskApi, basename="taskapi")
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("guddi", include("rest_framework.urls"))
]
