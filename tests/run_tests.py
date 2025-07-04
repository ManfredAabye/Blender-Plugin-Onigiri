import pytest
import os

def execute():
    pytest.main([os.path.dirname(__file__)])