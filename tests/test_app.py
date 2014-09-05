from app import app


class TestApp():
    test_case = {
        'data': {
            'login': 'user',
            'password': 'password',
            'site': 'yandex.ru',
            'length': 10,
        },
        'result': '682ee27b6d',
    }

    def setUp(self):
        self.app = app.test_client()

    def test_page_not_found(self):
        assert 'Page not found!' in self.app.get('/smt_page').data.decode()

    def test_index(self):
        assert 'Get your password!' in self.app.get('/').data.decode()

    def test_show_pass(self):
        result = self.app.post(
            '/show', data=self.test_case['data'],
        )
        html_page = result.data.decode()
        assert 'Your password:' in html_page
        assert self.test_case['result'] in html_page

    def test_get_pass(self):
        result = self.app.post(
            '/get', data=self.test_case['data'],
        )
        assert self.test_case['result'] == result.data.decode()
