import os

import reflex as rx

config = rx.Config(
    app_name=os.getenv("APP_NAME", "reflex_poc"),
    api_url="http://0.0.0.0:8000",
    telemetry_enabled=False,
)
