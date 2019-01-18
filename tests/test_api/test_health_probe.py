# Copyright (c) 2019 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.


def test_health_probe(client):
    resp = client.get("/anteater/api/health?type=unknown")
    assert resp.status_code == 404
    resp = client.get("/anteater/api/health?type=liveness")
    assert resp.status_code == 200
