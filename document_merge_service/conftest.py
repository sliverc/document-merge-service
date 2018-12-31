import importlib
import inspect

import pytest
from factory.base import FactoryMetaClass
from pytest_factoryboy import register
from rest_framework_jwt import test


def register_module(module):
    for name, obj in inspect.getmembers(module):
        if isinstance(obj, FactoryMetaClass) and not obj._meta.abstract:
            # name needs to be compatible with
            # `rest_framework.routers.SimpleRouter` naming for easier testing
            base_name = obj._meta.model._meta.object_name.lower()
            register(obj, base_name)


register_module(
    importlib.import_module(
        ".api.factories", "document_merge_service"
    )
)


@pytest.fixture
def client():
    return test.APIJWTClient()


@pytest.fixture
def admin_client(db, admin_user, client):
    client.login(username=admin_user.username, password="password")
    return client
