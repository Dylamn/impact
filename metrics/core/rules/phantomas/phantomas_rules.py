from metrics.core.rules.make_rule import make_rule
from .assets_rules import rules as assets_rules

rules = {
    # |--------------
    # | Assets / Weight
    # |--------------
    **assets_rules,
    # |--------------
    # | DOM Rules
    # |--------------
    'dom_length': make_rule(
        title='DOM elements count',
        good_threshold=800,
        ok_threshold=1200,
        bad_threshold=1500,
        msg='A large DOM will increase memory usage, cause longer style'
            ' calculations and produce layout reflows.'
    ),
    'dom_max_depth': make_rule(
        title='DOM max depth',
        good_threshold=12,
        ok_threshold=16,
        bad_threshold=32,
        msg='A DOM with deep nested elements makes the CSS matching slower.'
    ),
    "dom_id_duplicated": make_rule(
        title='Duplicated IDs',
        good_threshold=0,
        ok_threshold=0,
        bad_threshold=1,
        msg='The id attribute specifies a unique id for an HTML element.'
            ' The value of the id attribute must be unique within the HTML document.'
            ' It is mainly used to point to a specific style declaration in a style'
            ' sheet. It is also used by JavaScript to access and manipulate the '
            ' element with the specific id.'
    ),
    "iframes_count": make_rule(
        title='Number of iframes',
        good_threshold=2,
        ok_threshold=4,
        bad_threshold=6,
        msg='iFrames are the most complex HTML elements. They are pages,'
            ' just like the main page, and the browser needs to create'
            ' a new page context, which has a cost.'
    ),
    # |--------------
    # | CSS
    # |--------------
    'inline_css': make_rule(
        title='Externalize inline style',
        good_threshold=20,
        ok_threshold=40,
        bad_threshold=70,
        msg='Make sure that the CSS is separate from the HTML code of'
            ' the page. If you include CSS in the body of the HTML file and'
            ' it is used for multiple pages, the code must be sent for each page'
            ' the user requests, increasing the amount of data sent. However, if the'
            ' CSS is in its own separate file, the browser can avoid requesting them'
            ' again by storing it in its local cache.'
    ),
    # |--------------
    # | Javascript
    # |--------------
    'accesses_count': make_rule(
        title='DOM access',
        good_threshold=500,
        ok_threshold=700,
        bad_threshold=1500,
        msg='This estimates the how much times the JavaScript interact with the DOM'
            ' The more your JavaScript code accesses the DOM, the slower the page '
            ' will load. Try to generate as much as possible your page statically'
            ' (from the server side).'
    ),
    'js_exec_duration': make_rule(
        title='Script execution duration',
        good_threshold=500,
        ok_threshold=1000,
        bad_threshold=2000,
        msg='This is the number of milliseconds (ms) spent by the browser on'
            ' JavaScript execution during the page load.'
    ),
    'synchronous_ajax': make_rule(
        title='Synchronous AJAX requests',
        good_threshold=0,
        ok_threshold=0,
        bad_threshold=1,
        msg="Making an XMLHttpRequest with the async option set to false is"
            " deprecated due to the negative effect to performances. The browser's"
            " main thread needs to stop everything until the response is received."
    ),

    # |--------------
    # | Server Config
    # |--------------
    'old_http_protocol': make_rule(
        title='Old HTTP protocol',
        good_threshold=4,
        ok_threshold=10,
        bad_threshold=50,
        msg="HTTP/2 is the latest version of the HTTP protocol. It is designed to"
            " optimize load speed. Below 5 requests, the benefits of HTTP/2"
            " are generally less significant."
    ),
    'old_tls_protocol': make_rule(
        title='Old TLS protocol',
        good_threshold=0,
        ok_threshold=5,
        bad_threshold=10,
        msg="Counts the number of domains that use TLS versions < 1.3. This is the "
            "latest version since 2018 and it includes a faster \"handshake\" "
            "technology. Also, The 1.0 and 1.1 versions are deprecated and are "
            "considered as unsafe. You must atleast use the version 1.2."
    ),
    'caching_disabled': make_rule(
        title='Caching disabled',
        good_threshold=2,
        ok_threshold=15,
        bad_threshold=30,
        msg="Counts the number of responses that has been implicitly disabled"
            " for cache (the `max-age` is set to 0)."
    ),
    'caching_not_specified': make_rule(
        title='Caching not specified',
        good_threshold=5,
        ok_threshold=10,
        bad_threshold=20,
        msg="When no caching is specified, each browser will handle it differently."
            " Most of the time, it will automatically add a cache for you,"
            " but not all the time. You'd better handle it yourself."
    ),
    # |--------------
    # | Requests
    # |--------------
    'requests': make_rule(
        title='Requests count',
        good_threshold=27,
        ok_threshold=80,
        bad_threshold=120,
        msg="The total number of HTTP requests a site has to deal with can have"
            " a massive impact on the overall loading speed as each request"
            " slows down the page loading."
    ),
    'domains': make_rule(
        title='Number of domains',
        good_threshold=3,
        ok_threshold=12,
        bad_threshold=30,
        msg="For each domain met, the browser needs to make a DNS look-up,"
            " which is slow. Avoid having to many different domains and the"
            " page should render faster."

    ),
    'not_found': make_rule(
        title='404 not found',
        good_threshold=0,
        ok_threshold=0,
        bad_threshold=1,
        msg="404 errors are never cached, so each time a not found is reached, this"
            "means that the server has been hit. Also no links must be broken"
            " on your page."
    ),
    'below_the_fold_images': make_rule(
        title='Below the fold images',
        good_threshold=1,
        ok_threshold=12,
        bad_threshold=30,
        msg="This is the number of images displayed below the fold that could be"
            " lazy-loaded. Lazily loading them can greatly improve the page speed."
    ),
}
