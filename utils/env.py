import os
from dotenv import load_dotenv

load_dotenv()


def get_base_url() -> str:
    url = (os.getenv("BASE_URL") or "").strip().rstrip("/")

    if not url:
        raise RuntimeError(
            "Defina BASE_URL no arquivo .env"
        )

    return url