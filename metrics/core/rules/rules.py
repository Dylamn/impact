from django.utils.translation import gettext_lazy as _

from .make_rule import make_rule

rules = {
    # |--------------
    # | DOM Rules
    # |--------------
    'dom_length': make_rule(
        title=_('DOM elements count'),
        good_threshold=800,
        ok_threshold=1200,
        bad_threshold=1500,
        msg=_(
            'A large DOM will increase memory usage, cause longer style'
            ' calculations and produce layout reflows.'
        )
    ),
    'dom_max_depth': make_rule(
        title=_('DOM max depth'),
        good_threshold=12,
        ok_threshold=16,
        bad_threshold=32,
        msg=_(
            'A DOM with deep nested elements makes the CSS matching slower.'
            ' It also slows down '
        )
    ),
    "dom_id_duplicated": make_rule(
        title=_('Duplicated IDs'),
        good_threshold=0,
        ok_threshold=0,
        bad_threshold=1,
        msg=_(
            'The id attribute specifies a unique id for an HTML element.'
            ' The value of the id attribute must be unique within the HTML document.'
            ' It is mainly used to point to a specific style declaration in a style'
            ' sheet. It is also used by JavaScript to access and manipulate the '
            ' element with the specific id.'
        )
    ),
    "iframes_count": make_rule(
        title=_('Number of iframes'),
        good_threshold=2,
        ok_threshold=4,
        bad_threshold=6,
        msg=_(
            'iFrames are the most complex HTML elements. They are pages,'
            ' just like the main page, and the browser needs to create'
            ' a new page context, which has a cost.'
        )
    ),
    # |--------------
    # | CSS
    # |--------------
    "inline_css": make_rule(
        title=_('Externalize inline style'),
        good_threshold=4,
        ok_threshold=8,
        bad_threshold=10,
        msg=_(
            'Make sure that the CSS is separate from the HTML code of'
            ' the page. If you include CSS in the body of the HTML file and'
            ' it is used for multiple pages, the code must be sent for each page'
            ' the user requests, increasing the amount of data sent. However, if the'
            ' CSS is in its own separate file, the browser can avoid requesting them'
            ' again by storing it in its local cache.'
        )
    ),
    # |--------------
    # | Javascript
    # |--------------
    'accesses_count': make_rule(
        title=_('DOM access'),
        good_threshold=500,
        ok_threshold=700,
        bad_threshold=1500,
        msg=_(
            'This estimates the how much times the JavaScript interact with the DOM'
            ' The more your JavaScript code accesses the DOM, the slower the page '
            ' will load. Try to generate as much as possible your page statically'
            ' (from the server side).'
        )
    ),
    'js_exec_duration': make_rule(
        title=_('Script execution duration'),
        good_threshold=500,
        ok_threshold=1000,
        bad_threshold=2000,
        msg=_(
            'This is the number of milliseconds (ms) spent by the browser on'
            ' JavaScript execution during the page load.'
        )
    ),
    'synchronous_ajax': make_rule(
        title=_('Synchronous AJAX requests'),
        good_threshold=0,
        ok_threshold=0,
        bad_threshold=1,
        msg=_(
            "Making an XMLHttpRequest with the async option set to false is"
            " deprecated due to the negative effect to performances. The browser's"
            " main thread needs to stop everything until the response is received."
        )
    ),
}
