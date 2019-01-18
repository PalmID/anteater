# Copyright (c) 2018 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.

import os

import pytest

from app import create_app


@pytest.fixture(scope="session")
def app():
    os.environ["FLASK_ENV"] = "testing"
    app = create_app()
    return app


@pytest.fixture()
def client(app):
    client = app.test_client()
    return client
