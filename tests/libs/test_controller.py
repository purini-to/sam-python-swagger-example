import json
import unittest
from tests.test_util import setup_env
from app.libs.controller import Controller


class TestController(unittest.TestCase):
    def setUp(self):
        setup_env(self)

    def test_ok(self):
        with self.env:
            self.assertDictEqual(Controller().ok({"message": "test"}), {
                "statusCode": 200,
                "body": json.dumps({
                    "message": "test",
                })
            })

    def test_bad(self):
        with self.env:
            self.assertDictEqual(Controller().bad({"errors": [1]}), {
                "statusCode": 400,
                "body": json.dumps({
                    "errors": [1],
                })
            })

    def test_notfound(self):
        with self.env:
            self.assertDictEqual(Controller().notfound({"message": "404"}), {
                "statusCode": 404,
                "body": json.dumps({
                    "message": "404",
                })
            })
