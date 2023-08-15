from Sort_Impl.sort_strategy import SortStrategy


class Sorter:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort(self, lst):
        self._strategy.sort(lst)
