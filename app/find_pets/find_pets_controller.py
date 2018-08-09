import re
import os
from pydash import pick, compact
from app.libs.controller import Controller, validate

PET_NAME = os.environ['PET_NAME']


def __to_array_fields(v):
    return compact(re.sub(r'\s*?,\s*', ',', v).split(','))

# バリデーション定義
schema = {
    'fields': {
        'type': 'list',
        'coerce': (str, __to_array_fields),
        'allowed': ['id', 'name'],
    },
}


class FindPetsController(Controller):
    """
    パスパラメータやクエリストリングからビジネスロジックの処理を呼び出すクラス
    バリデーション等も行う
    """

    @validate(schema)
    def handler(self, params):
        """
        コントローラの処理クラス
        Lambdaのhandlerから渡されたパラメータでビジネスロジックを呼び出す
            :param self: インスタンス
            :param params: パスパラメータとクエリストリングの辞書型
        """
        pets = self.__createPets()
        fields = params.get('fields')
        if fields:
            pets = self.__pickFields(pets, fields)
        return self.ok({
            "data": pets
        })

    def __pickFields(self, pets, fields):
        return list(map(lambda p: pick(p, fields), pets))

    def __createPets(self):
        """
        Petsデータを生成する
        """
        return [
            {
                "id": 1,
                "name": "{}_{}".format(PET_NAME, 1),
            },
            {
                "id": 2,
                "name": "{}_{}".format(PET_NAME, 2),
            },
            {
                "id": 3,
                "name": "{}_{}".format(PET_NAME, 3),
            },
            {
                "id": 4,
                "name": "{}_{}".format(PET_NAME, 4),
            },
            {
                "id": 5,
                "name": "{}_{}".format(PET_NAME, 5),
            },
        ]
