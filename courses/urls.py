from django.urls import path

from . import views

urlpatterns = [
    path(
        route='mine/',
        view=views.ManageCourseListView.as_view(),
        name='manage_course_list'
    ),
    path(
        route='create/',
        view=views.CourseCreateView.as_view(),
        name='course_create'
    ),
    path(
        route='<pk>/edit/',
        view=views.CourseUpdateView.as_view(),
        name='course_edit'
    ),
    path(
        route='<pk>/delete/',
        view=views.CourseDeleteView.as_view(),
        name='course_delete'
    ),
    path(
        route='<pk>/module/',
        view=views.CourseModuleUpdateView.as_view(),
        name='course_module_update'
    ),
]
