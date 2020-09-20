import json

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build

class GoogleOAuth:
    """
    Specify details for the OAuth flow as well as the Google API to connect.
    Defaults to Google Analytics Management API (v3) using a client secret file (client_secret.json) located in the same directory.
    Credentials will be save to 'creds.json' for later future OAuth flows.
    """
    def __init__(self, SERVICE_NAME="analytics", SERVICE_VERSION="v3", AUTH_SCOPES="https://www.googleapis.com/auth/analytics.readonly", CLIENT_SECRET_PATH = "client_secret.json", CREDENTIALS_PATH="creds.json", SERVICE_ACCOUNT_KEY_PATH=None, SERVER_AUTH=True):
        self.SERVICE_NAME = SERVICE_NAME
        self.SERVICE_VERSION = SERVICE_VERSION
        self.AUTH_SCOPES = [AUTH_SCOPES]
        self.CLIENT_SECRET_PATH = CLIENT_SECRET_PATH
        self.CREDENTIALS_PATH = CREDENTIALS_PATH
        self.SERVICE_ACCOUNT_KEY_PATH = SERVICE_ACCOUNT_KEY_PATH
        self.SERVER_AUTH = SERVER_AUTH

    def run_oauth_flow(self):
        """
        Get credentials to authorize for a Google API.
        These credentials usually access resources on behalf of a user.

        Returns:
            Credentials which allow authorizing a service to a given Google API.
        """

        # OAuth from credentials file
        try:
            credentials = Credentials.from_authorized_user_file(self.CREDENTIALS_PATH)
        except FileNotFoundError:
            credentials = None
        except TypeError:
            credentials = None
        except ValueError:
            raise ValueError(
            "The credentials file '{}' is not in the expected format. Please provide a valid file format.".format(self.CREDENTIALS_PATH)
            )
        if credentials:
            return credentials
        
        # OAuth from service account key file  
        try:
            credentials = ServiceAccountCredentials.from_json_keyfile_name(
                self.SERVICE_ACCOUNT_KEY_PATH, scopes=self.AUTH_SCOPES
            )
        except TypeError:
            credentials = None
        except FileNotFoundError:
            credentials = None
        except ValueError:
            raise ValueError(
                "The credential type specified in the service account key file '{}' is not 'service_account'. Please provide a valid service account key file.".format(self.SERVICE_ACCOUNT_KEY_PATH)
            )
        except KeyError:
            raise KeyError(
                "One of the expected keys is not present in the service account key file '{}'. Please provide a valid service account key file.".format(self.SERVICE_ACCOUNT_KEY_PATH)
            )
        if credentials:
            return credentials

        # OAuth from client secret file
        try:
            flow = InstalledAppFlow.from_client_secrets_file(
                client_secrets_file=self.CLIENT_SECRET_PATH, scopes=self.AUTH_SCOPES
            )
        except FileNotFoundError:
            raise FileNotFoundError(
                "Please provide a valid client secret file as {}".format(self.CLIENT_SECRET_PATH)
            )

        if self.SERVER_AUTH:
            credentials = flow.run_local_server()
        else:
            credentials = flow.run_console()

        # Save credentials locally for later use
        creds_data = {
            "client_id": credentials.client_id,
            "client_secret": credentials.client_secret,
            "scopes": credentials.scopes,
            "token": None,
            "refresh_token": credentials.refresh_token,
            "token_uri": credentials.token_uri,
        }

        with open(self.CREDENTIALS_PATH, 'w') as creds_dump:
            json.dump(creds_data, creds_dump)

        return credentials

    def build_service(self, credentials):
        """
        Get a service that communicates to a Google API.

        Args:
            credentials: Credentials based on OAuth 2.0 access and refresh tokens.

        Returns:
            A service that is connected to the specified API.
        """
        service = build(self.SERVICE_NAME, self.SERVICE_VERSION, credentials=credentials)
        return service
