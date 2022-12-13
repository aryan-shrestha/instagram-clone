from django import template
from django.contrib.auth import get_user_model

register = template.Library()

User = get_user_model()

@register.simple_tag
def is_followed(obj, method_name, user_id):
    print(obj, method_name, user_id)
    method = getattr(obj, method_name)
    return method(user_id)