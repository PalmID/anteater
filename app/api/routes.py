# Copyright (c) 2019 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.

from flask import Blueprint

from app.api import detection, extraction, health_probe

bp = Blueprint("api", __name__)

bp.add_url_rule(
    "/health",
    view_func=health_probe.HealthProbeView.as_view("health_probe"),
    methods=["GET"],
)

bp.add_url_rule(
    "/detection/jobs",
    view_func=detection.PalmDetectionJobsView.as_view("palm_detection_jobs"),
    methods=["POST"],
)
bp.add_url_rule(
    "/detection/jobs/<job_id>",
    view_func=detection.PalmDetectionJobView.as_view("palm_detection_job"),
    methods=["GET"],
)
bp.add_url_rule(
    "/extraction/jobs",
    view_func=extraction.RoiExtractionJobsView.as_view("roi_extraction_jobs"),
    methods=["POST"],
)
bp.add_url_rule(
    "/extraction/jobs/<job_id>",
    view_func=extraction.RoiExtractionJobView.as_view("roi_extraction_job"),
    methods=["GET"],
)
