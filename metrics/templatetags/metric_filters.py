from typing import Any

from django.template.defaulttags import register


@register.filter
def get_item(dictionary: dict, key) -> Any:
    """Get an item from a dictionary and return its value"""
    return dictionary.get(key)


@register.simple_tag
def get_note(rule, value) -> str:
    good_threshold = rule.get('good_threshold')
    ok_threshold = rule.get('ok_threshold')

    return "a" if value <= good_threshold else "b" if value <= ok_threshold else "c"
