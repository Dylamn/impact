from django.template.defaulttags import register
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _


@register.simple_tag
def display_input_error(error_code) -> str:
    """Displays an error message with the given error code"""
    message = ""

    if error_code == 'network':  # pragma: no cover
        message = _(
            "We cannot etablish a network connection with the requested website."
        )
    elif error_code == 'url':  # pragma: no cover
        message = _(
            "The URL that you requested is not available or malformed. Do not "
            "forget the `http(s)` prefix."
        )

    return format_html(
        '<div id="page_url_error" class="text-red-600 py-2">{}</div>',
        message
    )


@register.simple_tag
def get_note(rule, value) -> str:
    good_threshold = rule.get('good_threshold')
    ok_threshold = rule.get('ok_threshold')

    return "a" if value <= good_threshold else "b" if value <= ok_threshold else "c"
