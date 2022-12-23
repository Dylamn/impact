from .abstracts import MetricModuleBase


class DOMMetrics(MetricModuleBase):
    def __init__(self):
        self.wrap_key = 'dom'
        self.label = 'DOM'

    def get_metrics(self, phantomas_results):
        return self.wrap_metrics({
            'dom_length': phantomas_results.get_metric('DOMelementsCount'),
            'dom_max_depth': phantomas_results.get_metric('DOMelementMaxDepth'),
            'dom_id_duplicated': phantomas_results.get_metric('DOMidDuplicated'),
            'iframes_count': phantomas_results.get_metric('iframesCount'),
        })
