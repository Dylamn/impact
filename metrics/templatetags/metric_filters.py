from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.simple_tag
def get_note(rule, value):
    note = rule.get('note')(value)

    return note.lower() if isinstance(note, str) else note
