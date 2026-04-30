import logging
from pythonjsonlogger import jsonlogger


def configure_logging(service_name: str) -> None:
    handler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter("%(asctime)s %(levelname)s %(name)s %(message)s")
    handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.handlers = [handler]
    logger.setLevel(logging.INFO)
    logger.info("logging_configured", extra={"service": service_name})
