from abc import ABCMeta, abstractmethod

from phantomas.results import Results as PhantomasResults


class MetricModuleBase(metaclass=ABCMeta):
    _label: str
    _weight: int = 1
    _wrap_key: str

    @property
    def label(self) -> str:
        return self._label

    @label.setter
    def label(self, val: str):
        self._label = val

    @property
    def weight(self) -> int:
        return self._weight

    @weight.setter
    def weight(self, val: int):
        self._weight = val

    @property
    def wrap_key(self) -> str:
        return self._wrap_key

    @wrap_key.setter
    def wrap_key(self, val: str):
        self._wrap_key = val

    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, 'get_metrics') and callable(subclass.get_metrics)

    @abstractmethod
    def get_metrics(self, phantomas_results: PhantomasResults) -> dict:
        """Get and return the gathered metrics."""
        raise NotImplementedError

    def format_metrics(self, metrics: dict, **kwargs) -> dict:
        """Wraps the values of the metrics and prints the weight.

        The metrics, weight along with the label will be wrapped with the
        `wrap_key` property. `kwargs` can also be passed to add other keys.
        """
        return {
            self.wrap_key: {
                'label': self.label,
                'metrics': metrics,
                'weight': self.weight,
                **kwargs
            }
        }
