from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False


"""Aby użyć w template:

-> należy na górze template wpisać:
{% load template_utils %}

-> używa sie to jak zwykłego ifa, podając grupę, dla której chcemy, żeby było widoczne

{% if request.user|has_group:"patient" %}
       Opakowany kod
{% endif %}

"""