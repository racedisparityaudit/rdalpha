from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

class GoogleSheetImporter(object):

    # If modifying these scopes, delete your previously saved credentials
    SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
    CLIENT_SECRET_FILE = '../client_secret.json'
    APPLICATION_NAME = 'Race Disparity Audit'


    def get_credentials(self, clients_secret_file):
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """

        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'sheets.googleapis.com-race-disparity-audit-google-importer.json')

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(clients_secret_file, self.SCOPES, None)
            flow.user_agent = self.APPLICATION_NAME

            credentials = tools.run_flow(flow, store)
            print('Storing credentials to ' + credential_path)

        return credentials



    def main_function(self):
        """Shows basic usage of the Sheets API.

        Creates a Sheets API service object and prints the names and majors of
        students in a sample spreadsheet:
        https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
        """

        credentials = self.get_credentials(self.CLIENT_SECRET_FILE)
        http = credentials.authorize(httplib2.Http())
        discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                        'version=v4')
        service = discovery.build('sheets', 'v4', http=http,
                                  discoveryServiceUrl=discoveryUrl)

        spreadsheetId = '1f9wXG4MLytGgpkn_Yo5buDoH-IjFLfS9VSq4N5LTwbo'
        rangeName = 'Sheet1!A1:B2'
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheetId, range=rangeName).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
        else:
            print('Name, Major:')
            for row in values:
                # Print columns A and E, which correspond to indices 0 and 4.
                print('%s, %s' % (row[0], row[1]))



if __name__ == '__main__':
    m = GoogleSheetImporter()
    m.get_credentials(clients_secret_file=m.CLIENT_SECRET_FILE)