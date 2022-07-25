from typing import Any

from django.template.defaulttags import register


@register.filter
def get_item(dictionary: dict, key) -> Any:
    """Get an item from a dictionary and return its value"""
    return dictionary.get(key)


@register.simple_tag
def get_note(rule, value) -> str:
    note = rule.get('note')(value)

    return note.lower() if isinstance(note, str) else note
