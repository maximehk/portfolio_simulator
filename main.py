import pandas as pd
from portfolio_simulator.mortgage import MortgageFactory

if __name__ == "__main__":
    pd.options.display.float_format = "{:,.0f}".format
    pd.set_option("display.max_rows", None)

    mortgage = MortgageFactory(
        principal=537_000, rate=1.69 / 100, start_date="2021-12-01", months=240
    ).MakeGermanMortgage(initial_amortization_rate=2 / 100)
    print(mortgage.to_dataframe().tail())
