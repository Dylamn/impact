from .abstracts import MetricModuleBase


class RequestsMetrics(MetricModuleBase):
    def __init__(self):
        self.wrap_key = 'requests'
        self.label = self.wrap_key.capitalize()

    def get_metrics(self, phantomas_results):
        return self.wrap_metrics({
            'requests': phantomas_results.get_metric('requests'),
            'domains': phantomas_results.get_metric('domains'),
            'not_found': phantomas_results.get_metric('notFound'),

            'below_the_fold_images': phantomas_results.get_metric(
                'lazyLoadableImagesBelowTheFold'
            ),
        })
