from .abstracts import MetricModuleBase


class CSSMetrics(MetricModuleBase):
    def __init__(self):
        self.wrap_key = 'css'
        self.label = self.wrap_key.upper()

    def get_metrics(self, phantomas_results):
        return self.format_metrics({
            'inline_css': phantomas_results.get_metric('nodesWithInlineCSS'),
        })
