# Copyright (c) 2018 leosocy. All rights reserved.
# Use of this source code is governed by a MIT-style license
# that can be found in the LICENSE file.

from flask import Blueprint

from .views import PalmDetectionView, PalmExtractionView


bp = Blueprint('api', __name__)

bp.add_url_rule(
    '/detection',
    view_func=PalmDetectionView.as_view('palm_detection')
)
bp.add_url_rule(
    '/extraction',
    view_func=PalmExtractionView.as_view('palm_extraction')
)
