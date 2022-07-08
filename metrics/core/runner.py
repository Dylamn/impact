from .phantomas_wrapper import PhantomasWrapper
from .rules import rules


class Runner:
    url: str
    rules: dict
    options: dict

    def __init__(self, url: str, *, options: dict = None, custom_rules=None):
        if custom_rules is None:
            custom_rules = rules
        if options is None:
            options = {}

        self.url = url
        self.options = options
        self.rules_set = custom_rules
        self.results = {}
        self.results_rules = {}

    def start(self):
        self.results = PhantomasWrapper(self.url).run()

        return self.results

    def get_rules_from_results(self):
        for category in self.results.values():
            if not isinstance(category, dict) or 'metrics' not in category:
                continue
            if not isinstance(category['metrics'], dict):
                continue

            for metric_name in category['metrics'].keys():
                print(metric_name)
                if metric_name in self.rules_set:
                    self.results_rules[metric_name] = self.rules_set[metric_name]

        return self.results_rules
