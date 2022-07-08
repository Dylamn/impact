from schema import Schema

from metrics.core.phantomas_wrapper.metrics_modules import DOMMetrics


class TestDOMMetrics:
    @classmethod
    def setup_class(cls):
        """setup any state specific to the execution of the given class"""
        cls.metric_module = DOMMetrics()

        wrap_key = 'dom'
        label = wrap_key.upper()

        cls.schema = Schema({
            wrap_key: {
                'label': label,
                'metrics': {
                    'dom_length': int,
                    'dom_max_depth': int,
                    'dom_id_duplicated': int,
                    'iframes_count': int,
                }
            }
        })

    def test_css_metrics_class_initialization(self):
        expected_text = 'dom'

        assert self.metric_module.wrap_key == expected_text
        assert self.metric_module.label == expected_text.upper()

    def test_css_metrics_results(self, phantomas_results):
        results = self.metric_module.get_metrics(phantomas_results)

        self.schema.validate(results)
