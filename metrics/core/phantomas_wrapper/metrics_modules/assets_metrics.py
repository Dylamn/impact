from .abstracts import MetricModuleBase


class AssetsMetrics(MetricModuleBase):
    def __init__(self):
        self.wrap_key = 'assets'
        self.label = self.wrap_key.capitalize()

    def get_metrics(self, phantomas_results):
        return self.wrap_metrics({
            'content_length': phantomas_results.get_metric('contentLength'),
            'body_size': phantomas_results.get_metric('bodySize'),

            'assets': {
                'js_size': phantomas_results.get_metric('jsSize'),
                'html_size': phantomas_results.get_metric('htmlSize'),
                'css_size': phantomas_results.get_metric('cssSize'),
                'json_size': phantomas_results.get_metric('jsonSize'),
                'image_size': phantomas_results.get_metric('imageSize'),
                'video_size': phantomas_results.get_metric('videoSize'),
                'webfont_size': phantomas_results.get_metric('webfontSize'),
                'base64_size': phantomas_results.get_metric('base64Size'),
                'other_size': phantomas_results.get_metric('otherSize'),
            }
        })
