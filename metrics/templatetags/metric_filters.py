from typing import Any

from django.template.defaulttags import register


@register.filter
def get_item(dictionary: dict, key) -> Any:
    """Get an item from a dictionary and return its value"""
    return dictionary.get(key)
