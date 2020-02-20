import basetest


class TestCaseMono3(basetest.BaseTest):
    def setUp(self):
        super().setUp()
        self.setUpCF(
            "_610TestApp.mpk",
            env_vars={
                "DEPLOY_PASSWORD": self.mx_password,
                "DEVELOPMENT_MODE": True,
            },
        )
        self.startApp()

    def test_mono3(self):
        self.assert_app_running()
        self.assert_string_in_recent_logs("Selecting Mono Runtime: mono-3")
