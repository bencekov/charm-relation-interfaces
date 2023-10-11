"""This file defines the schemas for the provider and requirer sides of the session_auth interface.
It exposes two interfaces.schema_base.DataBagSchema subclasses called:
- ProviderSchema
- RequirerSchema

Examples:
    ProviderSchema:
        unit: <empty>
        app: {"login_browser_endpoint": "http://kratos-url:4433/self-service/login/browser",
              "sessions_endpoint": "http://kratos-url:4433/sessions/whoami"
              }

    RequirerSchema:
        unit: <empty>
        app: {"allowed_return_urls": [
                "example-application-url",
                ],
              }
"""

from pydantic import BaseModel, Field
from interface_tester.schema_base import DataBagSchema
from typing import List


class SessionAuthProvider(BaseModel):
    login_browser_endpoint: str = Field(
        description="Kratos endpoint used for user authentication"
    )
    sessions_endpoint: str = Field(
        description="Kratos endpoint used for authenticating session cookies"
    )


class SessionAuthRequirer(BaseModel):
    allowed_return_urls: List[str] = Field(
        description="List of allowed return urls for used by Oathkeeper clients"
    )


class ProviderSchema(DataBagSchema):
    """Provider schema for kratos_endpoints."""
    app: SessionAuthProvider


class RequirerSchema(DataBagSchema):
    """Requirer schema for kratos_endpoints."""
    app: SessionAuthRequirer
