from schema import Schema

from metrics.core.phantomas_wrapper.metrics_modules import CSSMetrics


class TestCSSMetrics:
    @classmethod
    def setup_class(cls):
        """setup any state specific to the execution of the given class"""
        cls.metric_module = CSSMetrics()

        wrap_key = 'css'
        label = wrap_key.upper()

        cls.schema = Schema({
            wrap_key: {
                'label': label,
                'weight': int,
                'metrics': {
                    'inline_css': int,
                }
            }
        })

    def test_css_metrics_class_initialization(self):
        expected_text = 'css'

        assert self.metric_module.wrap_key == expected_text
        assert self.metric_module.label == expected_text.upper()

    def test_css_metrics_results(self, phantomas_results):
        results = self.metric_module.get_metrics(phantomas_results)

        self.schema.validate(results)
