"""political_search_engine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls import url
from django.views import generic

urlpatterns = [
		# We should add authentication in case of api endpoints
    path('api/search/', include('search.urls')),
    path('admin/', admin.site.urls),
		url(r'^$', generic.TemplateView.as_view(template_name='index.html')),
		url('usageanalytics/', generic.TemplateView.as_view(template_name='usageanalytics.html')),
		url('timeanalytics/', generic.TemplateView.as_view(template_name='timeanalytics.html')),
		url('locanalytics/', generic.TemplateView.as_view(template_name='locanalytics.html')),
		url('search/', generic.TemplateView.as_view(template_name='index.html')),
		url('about/', generic.TemplateView.as_view(template_name='index.html')),
		url('tweet/', generic.TemplateView.as_view(template_name='index.html')),
		url('poi/', generic.TemplateView.as_view(template_name='index.html')),
]
