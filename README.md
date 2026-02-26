# EquityTools GitHub Repo

<img width="153" height="153" alt="jonathan_starr_headshot_small" src="https://github.com/user-attachments/assets/323fa881-15ec-4392-a2a8-623fcebd7bc8" />

Please visit me on LinkedIn: <https://www.linkedin.com/in/jonathan-starr-profile/>

## Feb 2026

## 📍 Roadmap

See the full roadmap here → [EquityTools Wiki](https://github.com/californiaroll/EquityTools/wiki)

## Tech Stack

Python, pandas, numpy, matplotlib, yfinance, pytest, scikit-learn, math

## 🏗️  Architecture Diagram

EquityTools is organized as a modular, extensible Python toolkit for equity analysis, valuation, volatility modeling, and technical charting. The project separates research notebooks, reusable library code, and tests, making it easy to explore ideas while maintaining a clean, production‑ready codebase.

📂 Project Structure
EquityTools/  
│  
├── README.md  
├── LICENSE  
├── pyproject.toml  
├── requirements.txt  
├── run_tests.ipynb  
│  
├── Notebooks/  
│   ├── etf_get_holdings.ipynb
│   ├── portfolio_calculate_sharpe_ratio.ipynb  
│   ├── portfolio_country_breakdown.ipynb  
│   ├─ ─ stock_annual_volatility.ipynb  
│   ├── stock_chart_with_rsi_and_bollinger.ipynb  
│   ├── stock_dcf_valuation1.ipynb  
│   ├── stock_jump_diffusion_option_pricing1.ipynb  
│   ├── stock_option_series_with_tests.ipynb  
│   ├── stock_option_val1_black_scholes.ipynb  
│   ├── stock_portfolio_simulations.ipynb  
│   ├── stock_predict_base.ipynb  
│   └── stock_predict_volatility.ipynb  
│  
├── Workflows/  
│   └── (GitHub Actions or automation workflows)  
│  
├── equitytools_local/  
│   │  
│   ├── __init__.py  
│   │  
│   ├── data.py  
│   │  
│   ├── modeling.py  
│   │  
│   └── plotting.py  
│   │  
│   ├── technical_indicators.py  
│   │   ├── add_sma()  
│   │   ├── add_ema()  
│   │   ├── add_rsi()  
│   │   ├── add_macd()  
│   │   ├── add_bollinger_bands()  
│   │   └── add_all_indicators()  
│  
└── tests/  
    ├── test_data.py  
    ├── test_modeling.py  
    └── test_plotting.py  


## Data Flow Overview

        +-------------------+  
        |   Data Sources    |  
        | (yfinance, CSVs)  |  
        +---------+---------+  
                  |  
                  v  
        +-------------------+  
        |   data.py         |  
        | Load & normalize  |  
        +---------+---------+  
                  |  
                  v  
        +-------------------------+  
        | technical_indicators.py |  
        | Compute TI features     |  
        +---------+---------------+  
                  |  
                  v  
        +-------------------+  
        |   modeling.py     |  
        | Predictive models |  
        +---------+---------+  
                  |  
                  v  
        +-------------------+  
        |   plotting.py     |  
        | Visualizations    |  
        +-------------------+  
  
## How to Run Tests
 ```DOS
pip install -r requirements.txt
pytest
 ```

## ☑️ /Notebooks/sstock_annual_volatility.ipynb
### User can change the ticker and start_date and end_date.   Annual volatility is calculated and charted for 5 day windows.

<img width="1072" height="662" alt="image" src="https://github.com/user-attachments/assets/00d0cab1-7512-413e-a5c3-b247d727eeec" />

<img width="1268" height="692" alt="image" src="https://github.com/user-attachments/assets/9b855550-e57c-41a8-8335-de30a994ce21" />

<img width="1203" height="386" alt="image" src="https://github.com/user-attachments/assets/632b39fe-1b11-435b-a4f9-0219b25afe93" />


## ☑️ /Notebooks/stock_dcf_valuation1.ipynb
### Basic DCF valuation implemented for stocks
### Weighted Average Cost of Capital is calculated automatically from yFinance statistics
### FCF is also downloaded from yFinance, and initial estimate for short term growth is based on most recent growth in FCF.

<img width="1046" height="601" alt="image" src="https://github.com/user-attachments/assets/a872bb15-3c10-4f22-bee5-89e169addee0" />

## ☑️ /Notebooks/stock_jump_diffusion_option_pricing1.ipynb
### Option pricing implementing Merton's jump diffusion technique.

### Output is a comparison of Jump Diffusion option valuation with Black-Scholes valuation.

<img width="963" height="267" alt="image" src="https://github.com/user-attachments/assets/aeb729a4-c6c8-4859-866b-c1edc3a85c31" />


## ☑️ /Notebooks/stock_option_series_with_tests.ipynb

### Gets the bid, ask, volume of trades and pricing for a whole series of options for an underlying stock.

<img width="772" height="503" alt="image" src="https://github.com/user-attachments/assets/7ad4583c-61ab-48cc-8918-4f4d4e680ff8" />


## ☑️ /Notebooks/stock_option_val1_black_scholes.ipynb
### Inputs

<img width="617" height="320" alt="image" src="https://github.com/user-attachments/assets/2a4f5ba9-e8fe-4747-9d2b-12834f26f3cb" />

### Risk Free rates are retrieved from yFinance

### Output is call, put, delta and gamma calulculations

<img width="1097" height="143" alt="image" src="https://github.com/user-attachments/assets/c904c3d9-4dd2-42b8-bbed-51fd638b44d3" />
<img width="1042" height="150" alt="image" src="https://github.com/user-attachments/assets/340ed788-56d1-4ca4-89e6-8f16eac71cc0" />

## ☑️ /Notebooks/stock_predict_base.ipynb
### User can change the ticker, and the output is the 95% confidence interval for the ticker entered by getting the current stock price and the calculated Beta for the stock from yFrinance.

<img width="712" height="567" alt="image" src="https://github.com/user-attachments/assets/503c7a83-f0df-4be3-85a4-cb197cbb3992" />

## ☑️ /Notebooks/stock_predict_volatility.ipynb
### User can change the ticker and start_date and end_date.  Histogfram of price changes calculated.

<img width="1157" height="667" alt="image" src="https://github.com/user-attachments/assets/2a89a26f-ee46-4306-a683-ad89c89b3ba0" />

<img width="1140" height="682" alt="image" src="https://github.com/user-attachments/assets/7b99b9a9-8688-4dea-8916-c31be65e19cc" />

## ☑️ Notebooks/portfolio_country_breakdown.ipynb
### User can enter tickers and stock quantities and see their portfolio breakdown in $ invested by country

<img width="767" height="628" alt="image" src="https://github.com/user-attachments/assets/58cded60-de6f-4ee3-bd3a-cd3458d95cda" />

## ☑️ Notebooks/stock_chart_with_rsi_and_bollinger.ipynb
### User can enter ticker and get stock chart with RSI or stock chart with Bollinger Bands

####
Traditionally, an RSI reading of 70 or above indicates an overbought condition. A reading of 30 or below indicates an oversold condition. In addition to identifying overbought and oversold securities, the RSI can also indicate securities that may be primed for a trend reversal or a corrective pullback in price.

One bullish signal is when the RSI crosses below 30, where it would be considered oversold. But as noted above, bullish RSI signals are best used in uptrends. In a strong downtrend, prices can keep falling even after indicators are oversold, so trades based on that signal may have limited upside and go against the main trend.

Following a strong uptrend, another bullish RSI signal is a reversal after a decline to around 40 to 50, an area considered support during an uptrend. This often confirms a positive momentum shift back toward the uptrend after a pullback, signaling potential for continued gains.
####

<img width="1280" height="798" alt="image" src="https://github.com/user-attachments/assets/158339d3-0ca9-4b5d-9d10-13f51cf61a37" />

####
Bollinger Bands are a technical analysis tool that shows the volatility of an asset and potential overbought or oversold conditions by plotting two standard deviations away from a simple moving average.

When a stock's price is close to the upper Bollinger Band, it might be overbought; if it's near the lower band, it might be oversold, signaling potential trading opportunities.

Bollinger Bands work best as a secondary indicator, providing confirmation when used alongside other tools like relative strength index (RSI).

Widening bands indicate rising market volatility and may precede significant price moves, while narrowing bands suggest decreasing volatility and a possible impending breakout.

Trading platforms often include Bollinger Bands as a feature, allowing easy visualization of price movements and adaptability to different market conditions.
####

<img width="1212" height="623" alt="image" src="https://github.com/user-attachments/assets/d99603d8-abb9-4d23-862e-b181a0eb2ce9" />

## ☑️ Notebooks/etf_get_holdings.ipynb
### User can enter etf ticker and get the top holding for the ETF by market weight and a breakdown of the sectors in the ETF.

<img width="975" height="827" alt="image" src="https://github.com/user-attachments/assets/9eea3b1c-da70-43db-b7e5-1d4ff188b1bd" />

<img width="978" height="838" alt="image" src="https://github.com/user-attachments/assets/27915ae0-0a89-468b-9235-9e0fad7ddde0" />






