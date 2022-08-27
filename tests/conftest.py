import pytest
from rest_framework.test import APIClient
from model_bakery import baker


@pytest.fixture
def api_client():
    """Fixture for APIClient"""
    return APIClient()


@pytest.fixture
def course_factory():
    """Fixture for course factory"""
    def factory(*args, **kwargs):
        return baker.make('Course', *args, **kwargs)
    return factory


@pytest.fixture
def student_factory():
    """Fixture for student factory"""
    def factory(*args, **kwargs):
        return baker.make('Student', *args, **kwargs)
    return factory
