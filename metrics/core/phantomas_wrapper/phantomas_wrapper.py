from phantomas import Phantomas

from .metrics_modules import (
    CSSMetrics,
    DOMMetrics,
    JavascriptMetrics,
    MetricModuleBase,
)


class PhantomasWrapper:
    modules = [
        DOMMetrics,
        CSSMetrics,
        JavascriptMetrics,
    ]

    def __init__(self, url):
        self.phantomas = Phantomas(
            url=url,
            modules=['headers', 'requestsStats']
        )
        self.results = {}

    def run(self):
        """Start Phantomas and gather metrics."""
        phantomas_results = self.phantomas.run()

        for module in self.modules:
            if not issubclass(module, MetricModuleBase):
                continue
            mod_instance = module()

            self.results |= mod_instance.get_metrics(phantomas_results)

        return self.results
