from abc import ABCMeta, abstractmethod

from phantomas.results import Results as PhantomasResults


class MetricModuleBase(metaclass=ABCMeta):
    _label: str
    _wrap_key: str

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, val):
        self._label = val

    @property
    def wrap_key(self):
        return self._wrap_key

    @wrap_key.setter
    def wrap_key(self, val):
        self._wrap_key = val

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
                hasattr(subclass, 'get_metrics')
                and callable(subclass.get_metrics)
        )

    @abstractmethod
    def get_metrics(self, phantomas_results: PhantomasResults):
        """Get and return the gathered metrics."""
        raise NotImplementedError

    def format_metrics(self, metrics: dict):
        """Format the values of the given dict by wrapping them `wrap_key` property"""
        return {
            self.wrap_key: {
                'label': self.label,
                'metrics': metrics,
            }
        }
