from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path(
        route='room/<int:course_id>/',
        view=views.course_chat_room,
        name='course_chat_room'
    )
]
