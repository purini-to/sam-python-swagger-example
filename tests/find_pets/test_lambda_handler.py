import json
import unittest
from unittest.mock import patch
from tests.test_util import setup_env


class TestLambdaHandler(unittest.TestCase):
    def setUp(self):
        setup_env(self)

    @patch("app.get_pet.lambda_handler.GetPetController")
    def test_lambda_handler(self, mock_controller):
        with self.env:
            instance = mock_controller.return_value
            instance.handler.return_value = {
                "statusCode": 200,
                "body": 'test',
            }

            from app.get_pet.lambda_handler import lambda_handler
            res = lambda_handler({
                'pathParameters': {
                    'id': '1',
                },
                'queryStringParameters': {
                    'test': 'text',
                },
                'path': 'https://localhost:3000/api/test'
            }, None)
            self.assertDictEqual(res, {
                "statusCode": 200,
                "body": 'test',
            })
            instance.handler.assert_called_with({
                'id': '1',
                'test': 'text',
            })
