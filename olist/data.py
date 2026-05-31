from pathlib import Path
import pandas as pd


class Olist:
    def ping(self):
        return "pong"
    """
    The Olist class provides methods to interact with Olist's e-commerce data.

    Methods:
        get_data():
            Loads and returns a dictionary where keys are dataset names (e.g., 'sellers', 'orders')
            and values are pandas DataFrames loaded from corresponding CSV files.

        ping():
            Prints "pong" to confirm the method is callable.
    """
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
        csv_path = Path.home() / ".workintech" / "olist" / "data" / "csv"
        data = {}

        for csv_file in csv_path.iterdir():
            table_name = csv_file.name
            table_name = table_name.replace("olist_","")
            table_name = table_name.replace("_dataset.csv","")
            table_name = table_name.replace(".csv","")

            data[table_name] = pd.read_csv(csv_file)

        return data



    
