import os

import reflex as rx

config = rx.Config(
    app_name=os.getenv("APP_NAME", "reflex_poc"),
    telemetry_enabled=False,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
