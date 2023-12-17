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


def api_setup():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    credentials = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file(
            "token.json", SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not credentials or not credentials.valid:

        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                r"spreadsheet-api\credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(r"spreadsheet-api\token.json", "w") as token:
            token.write(credentials.to_json())

    try:
        service = build("sheets", "v4", credentials=credentials)
        sheet = service.spreadsheets()

        result = (
            sheet.values()
            .get(spreadsheetId=SPREADSHEET_ID, range="Arkusz1!A1:C6")
            .execute()
        )

        values = result.get("values", [])

        if not values:
            print("No data found.")
            return

        print("\n")

        for row in values:
            for item in row:
                print(item, end="  ")
            print(end='\n')
    except HttpError as error:
        print(error)


if __name__ == "__main__":
    api_setup()
