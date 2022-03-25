from src.utils.common_logger import logger


class BaseInsightsDBError(Exception):
    def __init__(self, message: str, status_code: int = 400) -> None:
        self.message = message
        self.status_code = status_code
        logger.error(message)

    def __str__(self) -> str:
        return self.message


class ScraperError(BaseInsightsDBError):
    def __init__(self, message: str) -> None:
        super().__init__(message)
