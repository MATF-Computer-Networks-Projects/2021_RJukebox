import logging
import os
from datetime import datetime
import pathlib

def setup_logger():
    days_old = 3
    file_name = _get_filename()

    logFormatter = logging.Formatter('[%(levelname)s : %(funcName)s : %(lineno)d] %(message)s')

    fileHandler = logging.FileHandler(file_name, encoding='utf-8')
    fileHandler.setFormatter(logFormatter)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)

    logging.basicConfig(
        level=logging.INFO,
        format='[%(levelname)s : %(funcName)s : %(lineno)d] %(message)s',
        handlers=[
            fileHandler,
            consoleHandler
        ]
    )

    _clean_old_logs(days_old)


def _get_filename():
    base_name = "applicationLogs"
    today_date = datetime.today().strftime('%Y_%m_%d_%H_%M')

    return f"{base_name}_{today_date}.log"


def _clean_old_logs(days_old: int) -> None:
    logging.debug(f"Cleaning logs older than [{days_old}] days.")

    log_files = [entry.name for entry in os.scandir(os.getcwd()) if 'applicationLogs' in entry.name]

    for log_file in log_files:
        try:
            logging.debug(f"Found log file [{log_file}]")

            created_at = pathlib.Path(log_file).stat().st_ctime
            created_days_ago = (datetime.now() - datetime.fromtimestamp(created_at)).days
            logging.debug(f"Created [{created_days_ago}] days ago.")

            if created_days_ago < days_old:
                continue

            logging.debug(f"Deleting log file [{log_file}]")
            os.remove(log_file)
        except Exception as e:
            logging.exception(f"Error happened while deleting log file [{log_file}]: {e}")
