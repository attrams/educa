from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'course'

router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)

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
    ),
    path(
        route='',
        view=include(router.urls)
    )
]
