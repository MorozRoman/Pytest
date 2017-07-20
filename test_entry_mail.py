# -*- coding: utf-8 -*-
import pytest
from accounts import Accounts
from fixture import Fixture

@pytest.fixture
def app(request):
    fixture = Fixture()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_entry_mail(app):
    app.input_mail(Accounts(name="123", pas="123"))
    app.out()
