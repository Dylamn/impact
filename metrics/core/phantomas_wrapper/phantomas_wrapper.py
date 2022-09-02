from phantomas import Phantomas

from .metrics_modules import (
    CSSMetrics,
    DOMMetrics,
    JavascriptMetrics,
    MetricModuleBase,
    ServerConfigMetrics,
    RequestsMetrics
)


class PhantomasWrapper:
    modules = [
        DOMMetrics,
        CSSMetrics,
        JavascriptMetrics,
        ServerConfigMetrics,
        RequestsMetrics
    ]

    def __init__(self, url):
        self.phantomas = Phantomas(
            url=url,
        )
        self.results = {}

        # Monkey patch for Phantomas:
        # Here we access a protected member of the instance, but we don't have choice
        # since the wrapper is not up-to-date. The `reporter` option doesn't exist
        # anymore in the most recents versions of phantomas.
        if 'reporter' in self.phantomas._options:
            self.phantomas._options.pop('reporter')

    def run(self):
        """Start Phantomas and gather metrics."""
        phantomas_results = self.phantomas.run()

        for module in self.modules:
            if not issubclass(module, MetricModuleBase):
                continue

            mod_instance = module()
            self.results |= mod_instance.get_metrics(phantomas_results)

        return self.results
