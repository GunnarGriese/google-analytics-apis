from oauth import GoogleOAuth
from management_api import AnalyticsManagement

# Specify service and OAuth config
service_config = GoogleOAuth(
    SERVICE_NAME="analytics",
    SERVICE_VERSION="v3",
    AUTH_SCOPES="https://www.googleapis.com/auth/analytics.readonly",
    CLIENT_SECRET_PATH="tools@iih.json",
    CREDENTIALS_PATH="creds.json",
    SERVICE_ACCOUNT_KEY_PATH=None,
    SERVER_AUTH=True,
)

# Build service
api_service = AnalyticsManagement(
    service_config, account_id="130829", property_id="UA-130829-38", view_id="119395418"
)

# Get list of all accounts
accounts, account_items = api_service.list_accounts()
print(accounts)

# Access specific property
#prop = api_service.get_property()
# print(prop)

# Access goals for view
goals = api_service.get_goals()
print(goals)
