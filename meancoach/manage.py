#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    settings_module = os.environ.get('DJANGO_SETTINGS_MODULE', None)
    assert settings_module, "DJANGO_SETTINGS_MODULE environment variable not set"

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
