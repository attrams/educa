from django.urls import path

from . import views

urlpatterns = [
    path(
        route='register/',
        view=views.StudentRegistrationView.as_view(),
        name='student_registration'
    ),
]
