# -*- coding: utf-8 -*-
import pytest

from fixture.fixture import Fixture
from model.accounts import Accounts


@pytest.fixture
def app(request):
    fixture = Fixture()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_entry_mail(app):
    app.session.input_mail(Accounts(name="romik.1994", pas="89632224715r"))
    app.session.out_mail()
