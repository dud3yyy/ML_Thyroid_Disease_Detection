import pandas as pd
from abc import ABC, abstractmethod

# Abstract base class for Data Inspection Strategies
class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self, df: pd.DataFrame) -> None:
        """
        Perform a specific type of data insepction.
        
        Args:
            df (pd.DataFrame): the dataframe that we want to inspect.
        
        Returns:
            None
        """
        pass

class DataTypesInspection(DataInspectionStrategy):
    def inspect(self, df:pd.DataFrame) -> None:
        """
        Inspects data types and non-null counts.
        
        Args:
            df (pd.DataFrame): the dataframe that we want to inspect.
        
        Returns:
            None
        """
        print("\nData Types and Non-null counts:")
        print(df.info())


class SummaryStatisticsInspection(DataInspectionStrategy):
    def inspect(self, df:pd.DataFrame) -> None:
        """
        Inspects numerical and categorical features.
        
        Args:
            df (pd.DataFrame): the dataframe that we want to inspect.
        
        Returns:
            None
        """
        print("\nSummary statistics for Numerical Features:")
        print(df.describe())
        print("\nSummary statistics for Categorical Features:")
        print(df.describe(include=["O"]))
        


class DataInspector:
    def __init__(self, strategy:DataInspectionStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy:DataInspectionStrategy):
        self._strategy = strategy

    def execute_inspection(self, df:pd.DataFrame):
        self._strategy.inspect(df)


if __name__ == "__main__":
    df = pd.read_csv("C:/Users/arbru/OneDrive/Desktop/DS/ML_Thyroid_Disease_Detection/ML_Thyroid_Disease_Detection/src/extracted_data/hypothyroid.csv")
    inspector = DataInspector(DataTypesInspection())
    inspector.execute_inspection(df)

    # change the strategy to SS

    inspector.set_strategy(SummaryStatisticsInspection())
    inspector.execute_inspection(df)
