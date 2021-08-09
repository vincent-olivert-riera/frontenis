# This template tag is needed for production
# Add it to one of your django apps (/appdir/templatetags/render_vite_bundle.py, for example)

import json

from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def render_vite_bundle():
    """
    Template tag to render a vite bundle.
    Supposed to only be used in production.
    For development, see other files.
    """

    try:
        with open(f"{settings.VITE_APP_DIR}/../dist/manifest.json", "r") as fd:
            manifest = json.load(fd)
    except Exception as open_exception:
        raise RuntimeError(
            f"Vite manifest file not found or invalid. Maybe your {settings.VITE_APP_DIR}/dist/manifest.json file is empty?"
        ) from open_exception

    imports_files = "".join(
        [
            f'<script type="module" src="/static/{manifest[file]["file"]}"></script>'
            for file in manifest["src/main.js"]["imports"]
        ]
    )

    return mark_safe(
        f"""<script type="module" src="/static/{manifest['src/main.js']['file']}"></script>
        <link rel="stylesheet" type="text/css" href="/static/{manifest['src/main.js']['css'][0]}" />
        {imports_files}"""
    )
