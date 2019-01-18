from flasgger import Swagger

SWAGGER_CONFIG = Swagger.DEFAULT_CONFIG
SWAGGER_CONFIG.update(
    {
        "specs": [
            {
                "endpoint": "apispec_1",
                "route": "/anteater/apispec_1.json",
                "rule_filter": lambda rule: True,  # all in
                "model_filter": lambda tag: True,  # all in
            }
        ],
        "uiversion": 3,
        "openapi": "3.0.1",
        "static_url_path": "/anteater/flasgger_static",
        "specs_route": "/anteater/apidocs",
        "swagger_ui_bundle_js": "//unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js",
        "swagger_ui_standalone_preset_js": "//unpkg.com/swagger-ui-dist@3/swagger-ui-standalone-preset.js",
        "jquery_js": "//unpkg.com/jquery@2.2.4/dist/jquery.min.js",
        "swagger_ui_css": "//unpkg.com/swagger-ui-dist@3/swagger-ui.css",
    }
)
SWAGGER_DOCS_ROOT = "docs/"  # relative to the `app.root_path`
