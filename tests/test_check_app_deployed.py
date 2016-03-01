import unittest
import requests
import os


class CheckTestAppDeployedTest(unittest.TestCase):
    def test_app_deployed(self):
        # assumes the app route is coming from env var
        app_name = os.environ.get("APP_NAME")
        full_uri = "https://" + app_name + "." + os.environ.get("CF_DOMAIN") + "/xas/"

        r = requests.get(full_uri)
        assert r.status_code == 401