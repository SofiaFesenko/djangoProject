from dataclasses import dataclass
from typing import List

from loguru import logger as base_logger
from loguru._logger import Logger  # noqa

from utils.loggers import providers


@dataclass(frozen=True)
class LogSchema:
    """
    This class describes the scheme for creating a Log.
        - level: Name of log level
        - no: log weight
        - providers: - list of handler providers.
            The provider is responsible for where the logs will be written
    """

    level: str  # need to be unique
    no: int
    handlers: List[providers.BaseLogHandlerProvider]


class LogLevels:
    INFO = 'INFO_LOG'
    MIDDLEWARE_ERROR_HANDLER = 'MIDDLEWARE'
    USER = 'USER'


class Logging:
    """
    The severity levels

    TRACE 5
    DEBUG 10
    INFO 20
    SUCCESS 25
    WARNING 30
    ERROR 40
    CRITICAL 50
    """
    logger: Logger = None

    log_registry = [
        LogSchema(
            level=LogLevels.INFO,
            no=10,
            handlers=[providers.FileLogHandlerProvider(path='info.log')],
        ),
        LogSchema(
            level=LogLevels.MIDDLEWARE_ERROR_HANDLER,
            no=50,
            handlers=[
                providers.FileLogHandlerProvider(path='middleware_error.log'),
            ],
        ),
        LogSchema(
            level=LogLevels.USER,
            no=50,
            handlers=[providers.FileLogHandlerProvider(path='auth_module.log')],
        )
    ]

    @classmethod
    def __setup_loggers(cls):
        base_logger.configure(extra={"request_id": 'Out of request context'})

        for log_schema in cls.log_registry:
            base_logger.level(log_schema.level, no=log_schema.no)  # add level

            for log_provider in log_schema.handlers:  # add all providers
                log_provider.add_handler(base_logger, log_schema.level)

        return base_logger

    @classmethod
    def setup_logging(cls) -> Logger:
        if not cls.logger:
            cls.logger = cls.__setup_loggers()
        return cls.logger


logger = Logging.setup_logging()
