from jupyterworkflow.data import load_data
import pandas as pd

def test_fremont_data():
    data = load_data()
    assert all(data.columns == ['Fremont Bridge Total', 'Fremont Bridge East Sidewalk', 'Fremont Bridge West Sidewalk'])
    assert isinstance(data.index, pd.DatetimeIndex)