download:
  uv run freqtrade download-data --pairs BTC/USDC --exchange binance --days 5 -t 15m

download_range:
  uv run freqtrade download-data --pairs BTC/USDT --exchange binance --timerange 20200101- -t 1d

backtest:
  uv run freqtrade backtesting --config user_data/config.json --strategy FindEdge FindEdge2 --timerange 20200101-20260101 -i 1d

backtest-list:
  uv run freqtrade backtesting --config user_data/config.json --strategy-list FindEdge FindEdge2 --timerange 20200101-20260101 -i 1d

plot:
  uv run freqtrade plot-dataframe --strategy AwesomeStrategy -p BTC/ETH --timerange=20180801-20180805

plot2:
  uv run freqtrade plot-profit -p BTC/USDT --timeframe 1d

webserver:
  uv runfreqtrade webserver

list_data:
  uv run freqtrade list-data

show_timeseries:
  uv run freqtrade list-data --show-timerange

opt:
  uv run freqtrade hyperopt --strategy FindEdge --hyperopt-loss OnlyProfitHyperOptLoss --spaces buy --epochs 20 --random-state 42 --print-all

opt-see:
  uv run freqtrade hyperopt-list

quarto:
  uv run quarto preview


