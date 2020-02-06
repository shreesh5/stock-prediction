# run command: pip install alpha_vantage pandas pprint matplotlib
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import matplotlib.pyplot as plt


def query():
    ts = TimeSeries(key='G89M0HECMYPKA46T', output_format='pandas')
    data, meta_data = ts.get_intraday('AAPL', interval='60min', outputsize='full')
    pprint(data.head(100))  # prints the most recent 100 points
    data['4. close'].plot()
    plt.title('Intraday (60 min) AAPL')
    plt.show()


if __name__ == '__main__':
    query()