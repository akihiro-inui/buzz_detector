from typing import Optional
from abc import ABC, abstractmethod


class BaseScraper(ABC):
    """
    Base class for Scraper
    """
    def __init__(self):
        pass

    @abstractmethod
    def scrape(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def _save(self, output_directory: Optional[str], output_file_path: Optional[str]):
        """
        Save scrape result
        """
        raise NotImplementedError
