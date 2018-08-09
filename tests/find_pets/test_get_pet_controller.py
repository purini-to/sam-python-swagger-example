import json
import unittest
from tests.test_util import setup_env


class TestGetPetController(unittest.TestCase):
    def setUp(self):
        setup_env(self)

    def test_handler_required(self):
        with self.env:
            from app.get_pet.get_pet_controller import GetPetController
            res = GetPetController().handler({})
            self.assertEqual(res['statusCode'], 400)

    def test_handler_integer(self):
        with self.env:
            from app.get_pet.get_pet_controller import GetPetController
            res = GetPetController().handler({"id": "1abcd"})
            self.assertEqual(res['statusCode'], 400)

    def test_handler_ok(self):
        with self.env:
            from app.get_pet.get_pet_controller import GetPetController
            res = GetPetController().handler({"id": "123"})
            self.assertDictEqual(res, {
                "statusCode": 200,
                "body": json.dumps({
                    "id": 123,
                    "name": "{}_{}".format(self.env.get("PET_NAME"), 123),
                })
            })
