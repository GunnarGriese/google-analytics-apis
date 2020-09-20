import oauth

# Specify service and OAuth config
service_config = oauth.GoogleOAuth(SERVICE_NAME="analytics", SERVICE_VERSION="v3", AUTH_SCOPES="https://www.googleapis.com/auth/analytics.readonly", CLIENT_SECRET_PATH = "credentials/gunnar_project.json", CREDENTIALS_PATH="creds.json", SERVICE_ACCOUNT_KEY_PATH=None, SERVER_AUTH=False)
# Create credentials
creds = service_config.run_oauth_flow()
# Build service
management_api = service_config.build_service(creds)
# Get list of all accounts 
accounts = management_api.management().accounts().list().execute()
print(accounts)
