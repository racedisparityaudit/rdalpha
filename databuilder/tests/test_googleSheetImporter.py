import unittest
from unittest import TestCase
from databuilder.tools.GoogleSheetImporter import GoogleSheetImporter
from oauth2client.client import GoogleCredentials

class TestGoogleSheetImporter(TestCase):

    def test_import_data_frame_with_unemployment_example(self):
        importer = GoogleSheetImporter()
        # creds = importer.get_credentials(clients_secret_file='../client_secret.json')
        creds = GoogleCredentials.get_application_default()
        self.assertIsNotNone(creds)


    def test_import_data_frame_with_unemployment_example_2(self):
        importer = GoogleSheetImporter()
        # creds = importer.get_credentials(clients_secret_file='../client_secret.json')
        creds = GoogleCredentials.get_application_default()
        importer.main_function()
        self.assertIsNotNone(creds)

if __name__ == '__main__':
    unittest.main()