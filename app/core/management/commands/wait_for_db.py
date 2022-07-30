"""
Django command to wait to database to be available
"""

import time

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wait for db"""

    def handle(self, *args, **options):
        """Entrypoint for wait_for_db command"""
        self.stdout.write("Waiting for db...")

        is_db_up = False
        while is_db_up is False:
            try:
                self.check(databases=["default"])
                is_db_up = True
            except(Psycopg2Error, OperationalError):
                self.stdout \
                    .write("Database not ready, waiting for 2 second...")
                time.sleep(2)

        self.stdout.write(self.style.SUCCESS("Database is available"))
