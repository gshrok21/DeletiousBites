"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from website import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),
    path('menu/',views.menu),
    path('reservation/',views.reservation,name='reservation'),
    path('submit_booking',views.submit_booking),
    path('submit_review', views.submit_review),
    path('cancel_booking',views.cancel_booking),
    path('submit_registration',views.submit_registration),
    path('login_page',views.login_page),
    path('logout_page',views.logout_page)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)