from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^education$', TemplateView.as_view(template_name='education/index.html'), name='education'),
    url(r'^education/attainment$', TemplateView.as_view(template_name='education/attainment/index.html'), name='education_attainment'),
    url(r'^education/attainment/are-children-in-the-relevant-group-likely-to-have-better-or-worse-early-years-outcomes$', TemplateView.as_view(template_name='education/attainment/are_children_in_the_relevant_group_likely_to_have_better_or_worse_early_years_outcomes.html'), name='education_attainment_are_children_in_the_relevant_group_likely_to_have_better_or_worse_early_years_outcomes'),
]