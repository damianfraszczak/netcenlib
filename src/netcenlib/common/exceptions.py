"""Exception utilities."""
import logging
import sys
import traceback
from typing import Any, Optional

from rpasdt.gui.utils import show_error_dialog

logger = logging.getLogger("netcenlib")


def log_error(
    type: Optional[type] = None,
    exc: Optional[Exception] = None,
    exc_traceback: Optional[Any] = None,
    title: str = None,
):
    """
    Intended to be assigned to sys.exception as a hook.
    Gives programmer opportunity to do something useful with info from uncaught exceptions.

    Parameters
    type: Exception type
    value: Exception's value
    tb: Exception's traceback
    title: Additional title
    """
    sys_exc_type, sys_exc, sys_exc_traceback = sys.exc_info()
    type = type or sys_exc_type
    exc = exc or sys_exc
    exc_traceback = exc_traceback or sys_exc_traceback

    traceback_details = "\n".join(traceback.extract_tb(exc_traceback).format())

    error_msg = (
        "An error occurred!!!\n"
        f"Type: {type}\n"
        f"Value: {exc}\n"
        f"Traceback: {traceback_details}"
    )
    logger.error(error_msg, exc_info=(type, exc, exc_traceback))

    title = title or "Error occurred"
    show_error_dialog(title=title, error_msg=error_msg)
