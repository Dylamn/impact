from schema import Schema

from metrics.core.phantomas_wrapper.metrics_modules import RequestsMetrics


class TestRequestsMetrics:
    @classmethod
    def setup_class(cls):
        """setup any state specific to the execution of the given class"""
        cls.metric_module = RequestsMetrics()

        wrap_key = 'requests'
        label = wrap_key.capitalize()

        cls.schema = Schema({
            wrap_key: {
                'label': label,
                'weight': int,
                'metrics': {
                    'requests': int,
                    'domains': int,
                    'not_found': int,
                    'below_the_fold_images': int,
                }
            }
        })

    def test_css_metrics_class_initialization(self):
        expected_text = 'requests'

        assert self.metric_module.wrap_key == expected_text
        assert self.metric_module.label == expected_text.capitalize()

    def test_css_metrics_results(self, phantomas_results):
        results = self.metric_module.get_metrics(phantomas_results)

        self.schema.validate(results)
