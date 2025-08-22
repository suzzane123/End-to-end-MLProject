import os
import requests
import urllib.request as request
import zipfile
from mlProject import logger
from mlProject.utils.common import get_size
from mlProject.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        # Check content type first
        response = requests.head(self.config.source_URL)
        content_type = response.headers.get('Content-Type', '').lower()
        if 'zip' not in content_type and 'octet-stream' not in content_type:
            logger.error(f"Invalid content type: {content_type}. Expected zip or binary.")
            raise ValueError("Downloaded file is not a zip (invalid content type)")
        
        # Proceed with download
        logger.info(f"Downloading from {self.config.source_URL}...")
        filename, headers = request.urlretrieve(
            url=self.config.source_URL,
            filename=self.config.local_data_file
        )
        logger.info(f"Downloaded file: {filename} with info :\n{headers}")

    def extract_zip_file(self):
        
        """
        zip_file_path: str add some comment here
        Extracts the zip file into directory
        """

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f"Extracted zip file to {unzip_path}")