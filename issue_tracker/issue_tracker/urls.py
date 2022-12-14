"""issue_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from webapp.views import HomeView, IssueView, CreateView, UpdateView, DeleteView, SearchView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='index'),
    path('issue/<int:pk>', IssueView.as_view(), name='issue'),
    path('create/', CreateView.as_view(), name='create'),
    path('update/<int:pk>', UpdateView.as_view(), name='update'),
    path('delete/<int:pk>', DeleteView.as_view(), name='delete'),
    path('search/', SearchView.as_view(), name='search')
]