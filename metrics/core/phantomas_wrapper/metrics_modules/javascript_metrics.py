from .abstracts import MetricModuleBase


class JavascriptMetrics(MetricModuleBase):
    accesses_metrics = [
        'DOMinserts',
        'DOMmutationsAttributes',
        'DOMmutationsInserts',
        'DOMmutationsRemoves',
        'DOMqueriesByClassName',
        'DOMqueriesById',
        'DOMqueriesByQuerySelectorAll',
        'DOMqueriesByTagName',
        'eventsBound',
    ]

    def __init__(self):
        self.wrap_key = 'javascript'
        self.label = self.wrap_key.capitalize()

    def get_metrics(self, phantomas_results):
        accesses_count = 0

        for metric in self.accesses_metrics:
            accesses_count += phantomas_results.get_metric(metric)

        return self.wrap_metrics({
            'accesses_count': accesses_count,
            'js_exec_duration': phantomas_results.get_metric('scriptDuration'),
            'synchronous_ajax': phantomas_results.get_metric('synchronousXHR'),
        })
