"""
Generate a data directory to load shapefiles
"""
import shutil

from django.core.management.base import LabelCommand, CommandError

DEFAULT_SHAPEFILES_DIR = 'data/shapefiles'

class Command(LabelCommand):
    
    def handle_label(self, label, **options):
        shutil.copytree(DEFAULT_SHAPEFILES_DIR, label)