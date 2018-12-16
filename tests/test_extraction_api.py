# Copyright (c) 2018 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.


def test_create_palm_extraction_job(client):
    url = "/anteater/api/extraction"
    res = client.post(url, data={})
    assert res.status_code == 200


def test_get_palm_extraction_job(client):
    url = "/anteater/api/extraction?job_id={}".format("xxx")
    res = client.get(url)
    assert res.status_code == 200
    assert res.data.decode()