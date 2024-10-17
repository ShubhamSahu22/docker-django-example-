#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

    try:
        # Ensure Django is available
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Ensure it's installed and available "
            "on your PYTHONPATH environment variable. Did you activate a "
            "virtual environment?"
        ) from exc

    # Handle system arguments and execute
    try:
        execute_from_command_line(sys.argv)
    except Exception as exc:
        print(f"An error occurred while executing the command: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
