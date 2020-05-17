from django.test import TestCase


class TestTokenAction(TestCase):
    fixtures = ['user']

    def test_get_jwt_tokens(self):
        response = self.client.post('/api/v1/token/', {
            'username': 'user',
            'password': '123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        return response.data

    def test_refresh_jwt_token(self):
        tokens = self.test_get_jwt_tokens()
        refresh = tokens.get('refresh')
        response = self.client.post('/api/v1/token/refresh/', {
            'refresh': refresh
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
        return response.data.get('access')

    def test_verify_jwt_tokens(self):
        tokens = self.test_get_jwt_tokens()
        access_token = tokens.get('access')
        response = self.client.post('/api/v1/token/verify/', {
            'token': access_token
        })
        self.assertEqual(response.status_code, 200)

    def test_protected_record_access(self):
        tokens = self.test_get_jwt_tokens()
        access_token = tokens.get('access')
        auth_string = f'Bearer {access_token}'

        response = self.client.get('/api/v1/record/', HTTP_AUTHORIZATION=auth_string)
        self.assertEqual(response.status_code, 200)

    def test_protected_record_create(self):
        tokens = self.test_get_jwt_tokens()
        access_token = tokens.get('access')
        auth_string = f'Bearer {access_token}'

        response = self.client.post('/api/v1/record/', {'text': 'new text'}, HTTP_AUTHORIZATION=auth_string)
        self.assertEqual(response.status_code, 201)

    def test_protected_record_create_after_refresh(self):
        access_token = self.test_refresh_jwt_token()
        auth_string = f'Bearer {access_token}'

        response = self.client.post('/api/v1/record/', {'text': 'new text after refresh'},
                                    HTTP_AUTHORIZATION=auth_string)
        self.assertEqual(response.status_code, 201)
