# Copyright (c) 2018 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.

from flask import Blueprint

from .views import (
    PalmDetectionJobsView,
    PalmDetectionJobView,
    RoiExtractionImageView,
    RoiExtractionJobsView,
    RoiExtractionJobView,
)

bp = Blueprint("api", __name__)

bp.add_url_rule(
    "/detection/jobs",
    view_func=PalmDetectionJobsView.as_view("palm_detection_jobs"),
    methods=["POST"],
)
bp.add_url_rule(
    "/detection/jobs/<job_id>",
    view_func=PalmDetectionJobView.as_view("palm_detection_job"),
    methods=["GET"],
)
bp.add_url_rule(
    "/extraction/jobs",
    view_func=RoiExtractionJobsView.as_view("roi_extraction_jobs"),
    methods=["POST"],
)
bp.add_url_rule(
    "/extraction/jobs/<job_id>",
    view_func=RoiExtractionJobView.as_view("roi_extraction_job"),
    methods=["GET"],
)
bp.add_url_rule(
    "/extraction/jobs/<job_id>/roi",
    view_func=RoiExtractionImageView.as_view("roi_extraction_job_image"),
    methods=["GET"],
)
