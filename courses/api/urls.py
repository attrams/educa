from django.urls import path

from . import views

app_name = 'course'
urlpatterns = [
    path(
        route='subjects/',
        view=views.SubjectListView.as_view(),
        name='subject_list'
    ),
    path(
        route='subjects/<pk>/',
        view=views.SubjectDetailView.as_view(),
        name='subject_detail'
    )
]
