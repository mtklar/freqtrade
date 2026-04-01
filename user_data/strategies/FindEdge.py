import optuna
from pandas import DataFrame

from freqtrade.strategy import CategoricalParameter, IntParameter, IStrategy


class FindEdge(IStrategy):
    # class HyperOpt:
    #     def generate_estimator(dimensions, **kwargs):  # type: ignore
    #         return optuna.samplers.BruteForceSampler(seed=42)

    timeframe = "1d"
    startup_candle_count: int = 200

    stoploss = -0.99  # Required # Required

    edge = CategoricalParameter(
        ["edge1", "edge2", "edge3", "edge4", "edge5"], default="edge2", space="buy"
    )

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:

        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:

        if self.edge.value == "edge1":
            dataframe.loc[dataframe.index % 4 == 0, "enter_long"] = 1
        if self.edge.value == "edge2":
            dataframe.loc[dataframe.index % 8 == 0, "enter_long"] = 1
        if self.edge.value == "edge3":
            dataframe.loc[dataframe.index % 12 == 0, "enter_long"] = 1
        if self.edge.value == "edge4":
            dataframe.loc[dataframe.index % 16 == 0, "enter_long"] = 1
        if self.edge.value == "edge5":
            dataframe.loc[dataframe.index % 20 == 0, "enter_long"] = 1

        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:

        if self.edge.value == "edge1":
            dataframe.loc[dataframe.index % 4 == 1, "exit_long"] = 1
        if self.edge.value == "edge2":
            dataframe.loc[dataframe.index % 8 == 2, "exit_long"] = 1
        if self.edge.value == "edge3":
            dataframe.loc[dataframe.index % 12 == 3, "exit_long"] = 1
        if self.edge.value == "edge4":
            dataframe.loc[dataframe.index % 16 == 4, "exit_long"] = 1
        if self.edge.value == "edge5":
            dataframe.loc[dataframe.index % 20 == 5, "exit_long"] = 1

        return dataframe
