import os
import pandas as pd
from abc import ABC, abstractmethod
import zipfile

class DataIngestor(ABC):
    @abstractmethod
    def ingest_data(self, file_path:str) -> pd.DataFrame:
        """abstract method used for data ingestion"""
        pass


class ZipDataIngestor(DataIngestor):
    def ingest_data(self, file_path:str) -> pd.DataFrame:
        """Method used to ingest data"""

        if not file_path.endswith('zip'):
            raise ValueError(f"No .zip files in {file_path}")
        
        with zipfile.ZipFile(file_path,'r') as zip_file:
            zip_file.extractall("extracted_data")

        extracted_files = os.listdir("extracted_data")
        csv_files = [f for f in extracted_files if f.endswith('.csv')]
        
        if len(csv_files)==0:
            raise ValueError("There are no csv files here!")
        if len(csv_files)>1:
            raise ValueError(f"There are {len(csv_files)} in this folder. Please specify which one to use!")
        
        csv_file_path = os.path.join("extracted_data", csv_files[0])
        print('here',csv_file_path)
        df = pd.read_csv(csv_file_path)

        return df

class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(file_extension:str) -> DataIngestor:
        """Static method used for all types of extensions"""
        if file_extension == ".zip":
            return ZipDataIngestor()
        else:
            raise ValueError(f"No ingestor available for file extension: {file_extension}")

# if __name__ == "__main__":

#     file_path = "/Users/arbru/OneDrive/Desktop/DS/ML_Thyroid_Disease_Detection/ML_Thyroid_Disease_Detection/data/archive.zip"

#     file_extension = os.path.splitext(file_path)[1]

#     data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)

#     df = data_ingestor.ingest_data(file_path)

#     print(df.head())
    