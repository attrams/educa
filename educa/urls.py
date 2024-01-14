"""
URL configuration for educa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from courses.views import CourseListView

urlpatterns = [
    path(
        route='__debug__/',
        view=include('debug_toolbar.urls')
    ),
    path(
        route='accounts/login/',
        view=auth_views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='accounts/logout/',
        view=auth_views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='admin/',
        view=admin.site.urls
    ),
    path(
        route='course/',
        view=include('courses.urls')
    ),
    path(
        route='students/',
        view=include('students.urls')
    ),
    path(
        route='api/',
        view=include('courses.api.urls', namespace='api')
    ),
    path(
        route='',
        view=CourseListView.as_view(),
        name='course_list'
    )
]

if settings.DEBUG:
    urlpatterns += static(
        prefix=settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
