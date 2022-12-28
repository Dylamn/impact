from metrics.utils import calculate_note, calculate_metric_score
from .phantomas_wrapper import PhantomasWrapper
from .rules import phantomas_rules


class Runner:
    url: str
    rules: dict
    options: dict

    def __init__(self, url: str, *, options: dict = None, custom_rules=None):
        if custom_rules is None:
            custom_rules = phantomas_rules
        if options is None:
            options = {}

        self.url = url
        self.options = options
        self.rules_set = custom_rules
        self.results = {}

    def start(self, *args, **kwargs):
        self.results = PhantomasWrapper(self.url).run(*args, **kwargs)

        self._merge_rules_with_results()
        global_score = self.calculate_global_score()

        return global_score, self.results

    def _merge_rules_with_results(self) -> None:
        """
        Merge the rules within the results and calculate the scores of the sections
        and their metrics individually.
        """
        for key, values in self.results.items():
            if not isinstance(values, dict) or 'metrics' not in values:
                continue
            if not isinstance(values['metrics'], dict):
                continue
            # Used to calculate the score of the section.
            # We'll append each metric score of the section.
            accumulated_scores = 0
            unused_metric = 0

            for metric_name, metric_value in values['metrics'].items():
                if metric_name not in self.rules_set:
                    unused_metric += 1
                    continue
                rule = self.rules_set[metric_name]

                if "rules" not in self.results[key]:
                    self.results[key]['rules'] = {}

                # Append the rule (title, message, thresholds...)
                self.results[key]['rules'].setdefault(metric_name, rule)
                # Append the actual score of the metric
                score = calculate_metric_score(
                    metric_value, rule['good_threshold'], rule['bad_threshold']
                )
                # dom/rules/dom_length/score
                self.results[key]['rules'][metric_name]['score'] = score
                accumulated_scores += score

            # Calculate the score of a section (javascript, DOM, CSS, etc...).
            section_score = round(
                accumulated_scores / (len(values['metrics']) - unused_metric)
            )
            self.results[key]['score'] = section_score
            self.results[key]['note'] = calculate_note(section_score)

    def calculate_global_score(self) -> int:
        """Calculate the global score."""
        total_score = 0
        n_sections = 0
        for values in self.results.values():
            total_score += values.get('score', 0)
            n_sections += 1

        return round(total_score / n_sections)
