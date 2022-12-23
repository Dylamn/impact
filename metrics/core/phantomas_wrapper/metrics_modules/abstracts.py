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
        return hasattr(subclass, 'get_metrics') and callable(subclass.get_metrics)

    @abstractmethod
    def get_metrics(self, phantomas_results: PhantomasResults):
        """Get and return the gathered metrics."""
        raise NotImplementedError

    def wrap_metrics(self, metrics: dict):
        """Wraps the values of the given dict with the `wrap_key` property value."""
        return {
            self.wrap_key: {
                'label': self.label,
                'metrics': metrics,
            }
        }
