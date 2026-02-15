import pandas as pd
import pytest
from unittest.mock import patch,  MagicMock

import sys, os
sys.path.append(os.path.abspath(".."))

import equitytools_local.plotting as plottingtools

from importlib import reload
reload(plottingtools)

def test_plot_confidence_interval_calls_matplotlib_correctly():
    ticker = "AAPL"
    ci_range = (80, 150)
    current_price = 120

    with patch("equitytools_local.plotting.plt.bar") as mock_bar, \
         patch("equitytools_local.plotting.plt.title") as mock_title, \
         patch("equitytools_local.plotting.plt.show") as mock_show:

        plottingtools.plot_confidence_interval(ticker, ci_range, current_price)

        mock_bar.assert_called_once_with(
            ['2.5% Result', 'Current Stock Price', '97.5% Result'],
            [ci_range[0], current_price, ci_range[1]],
            color='gray'
        )

        mock_title.assert_called_once_with(
            '95% Confidence Interval for One Year Out - ' + ticker
        )

        mock_show.assert_called_once()


