"""Environment helpers: load ``.env`` and resolve ``BASE_URL``."""

import os
from dotenv import load_dotenv

load_dotenv()


def get_base_url() -> str:
    """Return ``BASE_URL`` from the environment (required, no trailing slash)."""
    url = (os.getenv("BASE_URL") or "").strip().rstrip("/")

    if not url:
        raise RuntimeError(
            "Set BASE_URL in your .env file"
        )

    return url