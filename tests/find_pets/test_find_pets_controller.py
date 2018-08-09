import json
import unittest
from tests.test_util import setup_env


class TestFindPetsController(unittest.TestCase):
    def setUp(self):
        setup_env(self)

    def test_handler_fields_allow(self):
        with self.env:
            from app.find_pets.find_pets_controller import FindPetsController
            res = FindPetsController().handler({"fields": "test,id"})
            self.assertEqual(res['statusCode'], 400)

            res = FindPetsController().handler({"fields": "name,test"})
            self.assertEqual(res['statusCode'], 400)

            res = FindPetsController().handler({"fields": "name,id,   a"})
            self.assertEqual(res['statusCode'], 400)

    def test_handler_ok(self):
        with self.env:
            pet_name = self.env.get('PET_NAME')

            from app.find_pets.find_pets_controller import FindPetsController
            res = FindPetsController().handler({})
            self.assertDictEqual(res, {
                "statusCode": 200,
                "body": json.dumps({
                    "data": [
                        {
                            "id": 1,
                            "name": "{}_{}".format(pet_name, 1),
                        },
                        {
                            "id": 2,
                            "name": "{}_{}".format(pet_name, 2),
                        },
                        {
                            "id": 3,
                            "name": "{}_{}".format(pet_name, 3),
                        },
                        {
                            "id": 4,
                            "name": "{}_{}".format(pet_name, 4),
                        },
                        {
                            "id": 5,
                            "name": "{}_{}".format(pet_name, 5),
                        },
                    ]
                })
            })

    def test_handler_ok_fields(self):
        with self.env:
            pet_name = self.env.get('PET_NAME')

            from app.find_pets.find_pets_controller import FindPetsController
            res = FindPetsController().handler({"fields": "id"})
            self.assertDictEqual(res, {
                "statusCode": 200,
                "body": json.dumps({
                    "data": [
                        {
                            "id": 1,
                        },
                        {
                            "id": 2,
                        },
                        {
                            "id": 3,
                        },
                        {
                            "id": 4,
                        },
                        {
                            "id": 5,
                        },
                    ]
                })
            })
