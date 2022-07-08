from schema import Schema

from metrics.core.phantomas_wrapper.metrics_modules import JavascriptMetrics


class TestJavascriptMetrics:
    @classmethod
    def setup_class(cls):
        """setup any state specific to the execution of the given class"""
        cls.metric_module = JavascriptMetrics()

        wrap_key = 'javascript'
        label = wrap_key.capitalize()

        cls.schema = Schema({
            wrap_key: {
                'label': label,
                'metrics': {
                    'accesses_count': int,
                    'js_exec_duration': int,
                    'synchronous_ajax': int,
                }
            }
        })

    def test_css_metrics_class_initialization(self):
        expected_text = 'javascript'

        assert self.metric_module.wrap_key == expected_text
        assert self.metric_module.label == expected_text.capitalize()

    def test_css_metrics_results(self, phantomas_results):
        results = self.metric_module.get_metrics(phantomas_results)

        self.schema.validate(results)
