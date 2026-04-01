from functools import reduce

import optuna
import pandas as pd
import talib.abstract as ta
from pandas import DataFrame

import freqtrade.vendor.qtpylib.indicators as qtpylib
from freqtrade.strategy import IntParameter, IStrategy


class SimpleSMA(IStrategy):
    class HyperOpt:
        def generate_estimator(dimensions: list["Dimension"], **kwargs):
            return optuna.samplers.BruteForceSampler(seed=42)

    timeframe = "1d"
    startup_candle_count: int = 200

    stoploss = -0.99  # Required # Required

    # NOTE: epochs = 200 - 2 = 198
    buy_sma = IntParameter(2, 200, default=40, space="buy")

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # generate values for technical analysis indicators
        frames = [dataframe]
        for val in self.buy_sma.range:
            frames.append(
                DataFrame({f"buy_sma_{val}": ta.SMA(dataframe, timeperiod=val)})
            )

        # Combine all dataframes, and reassign the original dataframe column
        dataframe = pd.concat(frames, axis=1)

        # for val in self.buy_sma.range:
        #     dataframe[f"buy_sma_{val}"] = ta.SMA(dataframe, timeperiod=val)

        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # generate entry signals based on indicator values
        # dataframe.loc[
        #     (
        #         qtpylib.crossed_above(
        #             dataframe["close"], dataframe[f"buy_sma_{self.buy_sma.value}"]
        #         )
        #     ),
        #     "enter_long",
        # ] = 1

        conditions = []
        # GUARDS AND TRENDS
        # TRIGGERS
        conditions.append(
            qtpylib.crossed_above(
                dataframe["close"], dataframe[f"buy_sma_{self.buy_sma.value}"]
            )
        )

        # Check that volume is not 0
        # conditions.append(dataframe["volume"] > 0)

        if conditions:
            dataframe.loc[reduce(lambda x, y: x & y, conditions), "enter_long"] = 1

        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # generate exit signals based on indicator values
        # dataframe.loc[
        #     (
        #         qtpylib.crossed_below(
        #             dataframe["close"], dataframe[f"buy_sma_{self.buy_sma.value}"]
        #         )
        #     ),
        #     "exit_long",
        # ] = 1

        conditions = []
        # GUARDS AND TRENDS
        # TRIGGERS
        conditions.append(
            qtpylib.crossed_below(
                dataframe["close"], dataframe[f"buy_sma_{self.buy_sma.value}"]
            )
        )

        # Check that volume is not 0
        # conditions.append(dataframe["volume"] > 0)

        if conditions:
            dataframe.loc[reduce(lambda x, y: x & y, conditions), "exit_long"] = 1

        return dataframe
