import logging
import json

class JsonFormatter(logging.Formatter):
    def format(self, record):
        if isinstance(record.msg, dict):
            record.msg = json.dumps(record.msg)
        return super().format(record)

def setup_logging(level: str):
    handler = logging.StreamHandler()
    formatter = JsonFormatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )
    handler.setFormatter(formatter)

    root = logging.getLogger()
    root.setLevel(level)
    root.handlers = [handler]
