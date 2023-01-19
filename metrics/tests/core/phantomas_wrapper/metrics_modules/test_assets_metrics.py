from schema import Schema

from metrics.core.phantomas_wrapper.metrics_modules import AssetsMetrics


class TestAssetsMetrics:
    @classmethod
    def setup_class(cls):
        """setup any state specific to the execution of the given class"""
        cls.metric_module = AssetsMetrics()

        wrap_key = 'assets'
        label = 'Assets'

        cls.schema = Schema({
            wrap_key: {
                'label': label,
                'weight': 4,
                'metrics': {
                    'content_length': int,
                    'body_size': int,

                    'assets': {
                        'js_size': int,
                        'html_size': int,
                        'css_size': int,
                        'json_size': int,
                        'image_size': int,
                        'video_size': int,
                        'webfont_size': int,
                        'base64_size': int,
                        'other_size': int,
                    }
                }}
        })

    def test_css_metrics_class_initialization(self):
        expected_text = 'assets'

        assert self.metric_module.wrap_key == expected_text
        assert self.metric_module.label == expected_text.capitalize()

    def test_css_metrics_results(self, phantomas_results):
        results = self.metric_module.get_metrics(phantomas_results)

        self.schema.validate(results)
