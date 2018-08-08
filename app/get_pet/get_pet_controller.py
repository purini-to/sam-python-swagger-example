import os
from app.libs.controller import Controller, validate

PET_NAME = os.environ['PET_NAME']

# バリデーション定義
schema = {
    'id': {
        'type': 'integer',
        'required': True,
        'coerce': int,
    },
}


class GetPetController(Controller):
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
        id = params['id']
        return self.ok({
            "id": id,
            "name": "{}_{}".format(PET_NAME, id),
        })
