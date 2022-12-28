from metrics.core.rules.make_rule import make_rule

rules = {
    'content_length': make_rule(
        title='content length (compressed page weight)',
        good_threshold=int(0.5 * 10 ** 6),  # x * 10 ** 6 => xMB
        ok_threshold=int(0.6 * 10 ** 6),
        bad_threshold=int(1 * 10 ** 6),
        msg="The weight/size off the compressed content of all responses, i.e. what"
            " was transferred in packets (bytes). The smallest is it, the faster a"
            " slow connection can load the page."
    ),
    'body_size': make_rule(
        title='Body size (final page weight)',
        good_threshold=int(1 * 10 ** 6),  # x * 10 ** 6 => xMB
        ok_threshold=int(1.4 * 10 ** 6),
        bad_threshold=int(2 * 10 ** 6),
        msg="The weight of the page with all assets (uncompressed). You must try to"
            " make it smaller as possible. In general, it must not exceed 1MB, which"
            " is already big enough for small connections that'll need some seconds"
            " to fully load the page."
    ),
}
