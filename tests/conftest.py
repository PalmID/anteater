# Copyright (c) 2018 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.

import pytest

from app import create_app


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.fixture
def client(app):
    client = app.test_client()
    return client
