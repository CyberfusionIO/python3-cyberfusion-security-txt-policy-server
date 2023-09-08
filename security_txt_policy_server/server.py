"""Run Starlette app using Uvicorn."""

import uvicorn

from security_txt_policy_server import app, settings


def main() -> None:
    """Run app using Uvicorn."""
    uvicorn.run(
        app,
        host=settings.LISTEN_HOST,
        port=settings.LISTEN_PORT,
        log_level="info",
        proxy_headers=bool(settings.TRUSTED_PROXY_ADDRESSES),
        forwarded_allow_ips=list(settings.TRUSTED_PROXY_ADDRESSES),
    )


if __name__ == "__main__":
    main()
