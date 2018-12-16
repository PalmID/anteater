# Copyright (c) 2018 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.


def test_create_palm_detection_job(client):
    url = "/anteater/api/detection"
    res = client.post(url, data={})
    assert res.status_code == 200


def test_get_palm_detection_job(client):
    url = "/anteater/api/detection?job_id={}".format("xxx")
    res = client.get(url)
    assert res.status_code == 200
    assert res.data.decode()
