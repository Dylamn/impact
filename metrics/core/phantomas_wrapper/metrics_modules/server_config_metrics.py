from .abstracts import MetricModuleBase


class ServerConfigMetrics(MetricModuleBase):
    def __init__(self):
        self.wrap_key = 'server_config'
        self.label = 'Server Config'

    def get_metrics(self, phantomas_results):

        return self.format_metrics({
            'old_http_protocol': phantomas_results.get_metric('oldHttpProtocol'),
            'old_tls_protocol': phantomas_results.get_metric('oldTlsProtocol'),
            'caching_disabled': phantomas_results.get_metric('cachingDisabled'),

            'caching_not_specified':
                phantomas_results.get_metric('cachingNotSpecified'),

        })
