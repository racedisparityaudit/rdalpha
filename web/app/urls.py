from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^a$', TemplateView.as_view(template_name='a.html'), name='a'),
    url(r'^b$', TemplateView.as_view(template_name='b.html'), name='b'),
    url(r'^c$', TemplateView.as_view(template_name='c.html'), name='c'),
    url(r'^homepage$', TemplateView.as_view(template_name='homepage.html'), name='homepage'),
    url(r'^education$', TemplateView.as_view(template_name='education.html'), name='education'),
]