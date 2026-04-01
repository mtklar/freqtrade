from pandas import DataFrame

from freqtrade.strategy import IStrategy


class FindEdge2(IStrategy):
    timeframe = "1d"
    startup_candle_count: int = 200

    stoploss = -0.99  # Required # Required

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:

        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:

        dataframe.loc[dataframe.index % 8 == 0, "enter_long"] = 1

        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:

        dataframe.loc[dataframe.index % 8 == 2, "exit_long"] = 1

        return dataframe
