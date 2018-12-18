# Copyright (c) 2018 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.

from flask import Blueprint

from .views import ApiRootView, PalmDetectionView, ROIExtractionView

bp = Blueprint("api", __name__)

bp.add_url_rule("/", view_func=ApiRootView.as_view("root"), methods=["GET"])
bp.add_url_rule(
    "/detection",
    view_func=PalmDetectionView.as_view("palm_detection"),
    methods=["GET", "POST"],
)
bp.add_url_rule(
    "/extraction",
    view_func=ROIExtractionView.as_view("roi_extraction"),
    methods=["GET", "POST"],
)
