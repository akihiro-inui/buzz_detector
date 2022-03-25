from typing import Optional, List
from Scweet.scweet import scrape
import pandas as pd
from Scweet.user import get_user_information, get_users_following, get_users_followers
from src.scraper.base import BaseScraper
from src.utils.error_handler import ScraperError


class TwitterScraper(BaseScraper):
    """
    Scraper for Twitter
    """
    def __init__(self, language: str):
        super().__init__()
        self.language = language

    def scrape(self,
               keywords: Optional[List[str]],
               start_date: str,
               stop_date: str,
               output_file_path: Optional[str]) -> pd.DataFrame:
        """
        Scrape Tweets
        :param keywords: List of keywords to search
        :param start_date: Search from this date. e.g. "2021-10-01"
        :param stop_date: Search until this date. e.g. "2021-10-04"
        :param output_file_path: Output file path to export scraper result
        :return: Dataframe
        """
        try:
            scrape_result = scrape(words=keywords,
                                   since=start_date,
                                   until=stop_date,
                                   from_account=None,
                                   interval=1,
                                   headless=False,
                                   display_type="Top",
                                   save_images=False,
                                   lang=self.language,
                                   resume=False,
                                   filter_replies=False,
                                   proximity=False,
                                   geocode=None)

            # Save result to file
            if output_file_path:
                self._save(scrape_result, output_file_path)

            return scrape_result

        except Exception as err:
            raise ScraperError(f"Failed to run Twitter Scraper: {err}")

    def _save(self, scrape_result: pd.DataFrame, output_file_path: str) -> None:
        """
        Save scrape result
        :param scrape_result: Result as dataframe
        :param output_file_path: Output file path to export
        """
        try:
            scrape_result.to_csv(output_file_path, index=False)
        except Exception as err:
            raise ScraperError(f"Failed to save Twitter scraper result: {err}")


if __name__ == "__main__":
    TSC = TwitterScraper(language="en")
    keywords = ['bitcoin', 'ethereum']
    start_date = "2021-10-01"
    stop_date = "2021-10-03"
    output_file_path = f"twitter_{keywords}_{start_date}_{stop_date}"

    TSC.scrape(keywords=keywords,
               start_date=start_date,
               stop_date=stop_date,
               output_file_path=output_file_path)
