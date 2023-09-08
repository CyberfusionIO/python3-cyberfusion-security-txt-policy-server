"""Starlette app."""

from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.routing import Route

from security_txt_policy_server.database import Database
from security_txt_policy_server.endpoints import SecurityTXTPolicy
from security_txt_policy_server.middleware import (
    InjectSecurityTXTPolicyMiddleware,
)

# Initialise app
#
# AFAIK, 'TrustedHostMiddleware' doesn't do anything when '*' is in 'allowed_hosts'.
# It's just here for consistency's sake.

middleware = [
    Middleware(InjectSecurityTXTPolicyMiddleware),
    Middleware(TrustedHostMiddleware, allowed_hosts=["*"]),
]
routes = [
    Route("/.well-known/security.txt", SecurityTXTPolicy, methods=["GET"])
]

app = Starlette(routes=routes, middleware=middleware)

# Add database to app

app.state.database = Database()  # type: ignore[has-type]
