import json
from cerberus import Validator


def _formatError(v):
    """
    エラーメッセージを整形してJSON用の辞書型に変換する
        :param v: バリデーションインスタンス
    """
    error_messages = v.errors
    errors = []
    for e in v._errors:
        errors.append({
            "field": e.field,
            "message": error_messages[e.field][0]
        })
        # エラーメッセージを順番に取得するために、一度取得したら削除して番号をズラす
        del error_messages[e.field][0]

    return errors


def validate(schema):
    def _validate(func):
        def wrapper(*args, **kwargs):
            v = Validator(schema)
            if not v.validate(args[1]):
                return args[0].bad({
                    "errors": _formatError(v)
                })
            args = list(args)
            args[1] = v.document
            return func(*args, **kwargs)
        return wrapper
    return _validate


class Controller:

    def ok(self, body):
        """
        200のOKレスポンスを返却する
            :param self: インスタンス
            :param body: ボディのJSONに変換する辞書型
        """
        return {
            "statusCode": 200,
            "body": json.dumps(body),
        }

    def bad(self, body):
        """
        400のBadRequestレスポンスを返却する
            :param self: インスタンス
            :param validated: ボディのJSONに変換する辞書型
        """
        return {
            "statusCode": 400,
            "body": json.dumps(body),
        }

    def notfound(self, body):
        """
        404のNotFoundレスポンスを返却する
            :param self: インスタンス
            :param body: ボディのJSONに変換する辞書型
        """
        return {
            "statusCode": 404,
            "body": json.dumps(body),
        }
