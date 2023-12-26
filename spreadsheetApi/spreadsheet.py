import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = "19VN0NjdMPcDckTxbwTvJ3OacA9KGAdP9jcZnbOzqocg"


class SheetApi:
    def __init__(self):

        self.credentials = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(r"spreadsheetApi\token.json"):
            self.credentials = Credentials.from_authorized_user_file(
                r"spreadsheetApi\token.json", SCOPES)

        # If there are no (valid) credentials available, let the user log in.
        if not self.credentials or not self.credentials.valid:

            if self.credentials and self.credentials.expired and self.credentials.refresh_token:
                self.credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    r"spreadsheetApi\credentials.json", SCOPES)
                self.credentials = flow.run_local_server(port=0)

            # Save the credentials for the next run
            with open(r"spreadsheetApi\token.json", "w") as token:
                token.write(self.credentials.to_json())

    def read(self, range: str):
        self.range = range

        try:
            service = build("sheets", "v4", credentials=self.credentials)
            sheet = service.spreadsheets()

            result = (
                sheet.values()
                .get(spreadsheetId=SPREADSHEET_ID, range=self.range)
                .execute()
            )

            values = result.get("values", [])

            if not values:
                print("No data found.")
                return

            return values

        except HttpError as error:
            print(error)
