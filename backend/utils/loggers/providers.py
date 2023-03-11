import os
from dataclasses import dataclass

from django.conf import settings


@dataclass(frozen=True)
class BaseLogHandlerProvider:
    """The provider is responsible for where the logs will be written"""

    @staticmethod
    def _make_filter(level: str):
        def log_filter(record):
            return record['level'].name == level

        return log_filter

    def add_handler(self, logger_adding_handler, level: str):
        pass


@dataclass(frozen=True)
class FileLogHandlerProvider(BaseLogHandlerProvider):
    path: str

    def add_handler(self, used_logger, level):
        # full path to log file
        path = os.path.join(settings.LOGS_DIR, self.path)
        used_logger.add(
            path,
            level=level,
            rotation="30 days",
            compression="zip",
            format="timestamp: {time}\nrequest_id: {extra[request_id]}\nmessage: {message}\n",
            backtrace=False,
            diagnose=True,
            catch=False,
            enqueue=True,
            # serialize=True,
            # colorize=True,
            filter=self._make_filter(level),
        )
