from app import app


class TestApp():
    test_case = {
        'data': {
            'login': 'user',
            'password': 'password',
            'site': 'yandex.ru',
            'length': 10,
        },
        'result': '0E8f1Ae2Cb',
        'result_when_ignore': '7D4e7Da2C3',
    }

    def setUp(self):
        self.app = app.test_client()

    def test_page_not_found(self):
        msg = 'Page not found!'
        assert msg in self.app.get('/smt_page').data.decode()

    def test_form(self):
        msg = 'The Form of the password generation'
        assert msg in self.app.get('/').data.decode()

    def test_result(self):
        result = self.app.post(
            '/result', data=self.test_case['data'],
        )
        html_page = result.data.decode()

        msg = 'Your new password'
        assert msg in html_page
        assert self.test_case['result'] in html_page

    def test_get(self):
        _data = self.test_case['data'].copy()

        result = self.app.post('/get', data=_data)
        assert self.test_case['result'] == result.data.decode()

        _data['ignore'] = True
        result = self.app.post('/get', data=_data)
        assert self.test_case['result_when_ignore'] == result.data.decode()
