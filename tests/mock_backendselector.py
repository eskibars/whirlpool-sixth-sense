class BackendSelectorMock:
    @property
    def brand(self):
        return "dummy_brand"

    @property
    def region(self):
        return "dummy_region"

    @property
    def base_url(self):
        return "http://dummy_base_url.com"

    @property
    def client_id(self):
        return "dummy_client_id"

    @property
    def client_secret(self):
        return "dummy_client_secret"
