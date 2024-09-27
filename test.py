import unittest
from app import app


class TestURLShortenerAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()  # Flask test client
        self.app.testing = True

    def test_shorten_url(self):
        """
        Test the /api/shorten endpoint to shorten a new URL.
        """
        response = self.app.post(
            '/api/shorten',
            json={'url': 'https://link.easyfit.fi/ls/click?upn=u001.1GB7ZOOWM9M8OF9pyuNwQwwZbr22dBJWTeYe2Tir-2BWkBxUalEvvDkqgf-2BGXLh5jMnkKO-2B9s03J0SZ5-2BQXi5R-2BYZV0dYOK3Q6JzskE9quOWvtgBAsh4qa-2Bcc-2FLLNJxVBZTlZDZtZojZ2QSJSbvBb-2FYaBqwCPpdRUPcpXpcqXOrI2BXh7gC0M6kto2FM9sMByu1AELCPX8eQ5Xv0RnbQBw1B7SvGp-2BEwE5t6p4e6ZZZnAN1HfqhlmchbfKeKFQz4NXAJZiyG4DvspVXEaoe3xrSg-3D-3Dyy4Y_aMc-2F08RjSMYuMSLWZvtiVQG9V5vKqQ9k0BbOfr3OLv951CFSVX3DGTtVb53e4aHKFBfdCxTfTp-2FztvNmwVKqMv-2BNjEaFvqXBiKmpAt4sbuf9TZv339fO-2Ffk070cGWA0B53onHiv0QdEpW4B-2FZJtu5gDhCGkUHN9jWeKAwRf9LpWp25KCpxSvMujMZsllMYkThaGdakTTONXd-2FXx5lhjL9et9bJQBYJCR97suLkCi0MQcL5hcwE9bFZ3g5SnRY-2BT3lSS8mIHRd3O91OE4xH1926r6u7iGRLg7cRsRQeKyP3-2FDqkFyqHLUodLbnx8oIaq8GgkWnnNl3cP5wmixIOyI2g-3D-3D'}  # Sending JSON request
        )

        # Checking the response code
        self.assertEqual(response.status_code, 200)

        # Get the JSON response and verify it contains the short URL
        response_json = response.get_json()
        self.assertIn('short_url', response_json)
        print(response_json)


if __name__ == '__main__':
    unittest.main()
