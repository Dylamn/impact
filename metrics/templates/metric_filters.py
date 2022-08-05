from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter(name='zip')
def zip_lists(a, b):
    return zip(a, b)
