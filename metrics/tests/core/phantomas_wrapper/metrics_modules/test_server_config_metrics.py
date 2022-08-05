from schema import Schema

from metrics.core.phantomas_wrapper.metrics_modules import ServerConfigMetrics


class TestServerConfigMetrics:
    @classmethod
    def setup_class(cls):
        """setup any state specific to the execution of the given class"""
        cls.metric_module = ServerConfigMetrics()

        wrap_key = 'server_config'
        label = 'Server Config'

        cls.schema = Schema({
            wrap_key: {
                'label': label,
                'metrics': {
                    'old_http_protocol': int,
                    'old_tls_protocol': int,
                    'caching_disabled': int,
                    'caching_not_specified': int,
                }
            }
        })

    def test_css_metrics_class_initialization(self):
        expected_key = 'server_config'
        expected_label = 'Server Config'
        assert self.metric_module.wrap_key == expected_key
        assert self.metric_module.label == expected_label

    def test_css_metrics_results(self, phantomas_results):
        results = self.metric_module.get_metrics(phantomas_results)

        self.schema.validate(results)
