import json
from app.get_pet.get_pet_controller import GetPetController
from logging import getLogger, INFO
logger = getLogger(__name__)
logger.setLevel(INFO)


def lambda_handler(event, context):
    """
    Lambdaが呼び出される最初の関数
    テストファーストを考え、基本はログ出力と必要なイベントパラメータの取得のみ行う
    バリデーション等はコントローラに委譲する
        :param event: Lambda呼び出しイベント
        :param context: Lambda呼び出し情報
    """
    p = event['pathParameters'] or {}
    q = event['queryStringParameters'] or {}
    params = {**p, **q}
    logger.info("path:{}".format(event['path']))
    logger.info("params:{}".format(params))

    return GetPetController().handler(params)
