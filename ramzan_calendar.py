from __future__ import print_function

import argparse
import pickle
import os.path

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from tqdm import tqdm

from make_events import get_events

SCOPES = ['https://www.googleapis.com/auth/calendar']


def main(arguments):
    """
    Create Sehr-o-Aftar Events on Google Calendar with 10 mins before reminder.
    """

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

    # Get service object to call apis
    service = build('calendar', 'v3', credentials=creds)
    for event in tqdm(get_events()):
        service.events().insert(calendarId=arguments.calendarId, body=event).execute()


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='Ramzan Calendar, Sehar-o-Aftar events creator')
    arg_parser.add_argument('calendarID', help='Enter the calendar ID')
    arguments = arg_parser.parse_args()

    main(arguments)
