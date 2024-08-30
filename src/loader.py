import pandas as pd


class NewsDataLoader:
    """
    NewsDataLoader class for loading rating, domain location, and traffic data.
    """

    def __init__(self, path):
        """
        Initialize a NewsDataLoader instance.

        Parameters:
            path (str): The path to the directory containing the csv files.
        """
        self.path = path
        self.data = None
        self.domain = None
        self.traffic = None

    def load_data(self):
        """
        Load rating data from the csv file.

        Returns:
            pandas.DataFrame: Rating data.
        """
        df = pd.read_csv(f"{self.path}/rating.csv")
        return df

    def load_domain_location(self):
        """
        Load domain location data from the csv file.

        Returns:
            pandas.DataFrame: Domain location data.
        """
        df = pd.read_csv(f"{self.path}/domains_location.csv")
        return df

    def load_traffic(self):
        """
        Load traffic data from the csv file.

        Returns:
            pandas.DataFrame: Traffic data.
        """
        df = pd.read_csv(f"{self.path}/traffic.csv")
        return df

    def load_title_content_similarity(self):
        """
        Load title content similarity data from the csv file.

        Returns:
            pandas.DataFrame: Title content similarity data.
        """
        df = pd.read_csv(f"{self.path}/title_content_similarity.csv")
        return df
