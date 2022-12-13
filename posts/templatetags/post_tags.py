from django import template
from django.contrib.auth import get_user_model

register = template.Library()

User = get_user_model()

@register.simple_tag
def is_liked(obj, method_name, id):
    user = User.objects.get(id=id)
    method = getattr(obj, method_name)
    return method(user)