# sam-python-swagger-example
sam + python + api gateway (swagger) boiler template

# 必要なライブラリ
* [Python 3 installed](https://www.python.org/downloads/)
* [Docker installed](https://www.docker.com/community-edition)
* [Python Virtual Environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
* [AWS SAM CLI](https://github.com/awslabs/aws-sam-cli)

# インストール方法

aws-sam-cli  
https://github.com/awslabs/aws-sam-cli#windows-linux-macos-with-pip

virtual-env  
https://virtualenv.pypa.io/en/stable/installation/

# virtual-env 使い方

virtual-envでPython3の環境を構築
```
virtualenv virtual-env
source virtual-env/bin/activate
# virtualenvから抜ける場合は以下
deactivate
```

# フォルダ構成

```bash
.
├── Makefile                    <-- タスクランナー定義ファイル
├── README.md
├── app                         <-- Lambdaのソースコードを配置するフォルダ
│   ├── __init__.py
│   ├── xxxxxx                  <-- Lambda Function
│   └── libs                    <-- 共通部品
├── constraints.txt             <-- Python依存関係バージョン固定ファイル
├── requirements.txt            <-- Python依存関係解決ファイル
├── template.yaml               <-- CloudFrontのテンプレートファイル
├── test_requirements.txt       <-- テスト時のPython依存関係解決ファイル
└── tests                       <-- 単体テストファイル
```

## 開発セットアップ方法

### 依存関係の解決

```bash
make dep
```

依存関係を追加したい場合は以下の手順に従うこと

1. モジュール名を`requirements.txt`に追記する(テスト用途の場合は`test_requirements.txt`)
2. モジュールをインストール
```bash
make dep
```
3. バージョン固定ファイルを更新
```bash
pip freeze > constraints.txt
```

### ユニットテスト

```bash
make test
# カバレッジあり(HTML)
python -m pytest tests -v --cov=app/ --cov-report html
# カバレッジなし
python -m pytest tests -v
```

### ローカル API Gateway 起動

```bash
export AWS_ACCESS_KEY_ID=<your access key id>
export AWS_SECRET_ACCESS_KEY=<your secret access key>
export AWS_DEFAULT_REGION=ap-northeast-1

make
# または
make start-api
```
アクセス：http://127.0.0.1:3000

## パッケージングとデプロイ

### パッケージング

```bash
make package
# カスタマイズ用
make package \
    TEMPLATE_PATH=template.yaml \
    PACKAGE_PATH=packaged.yaml \
    CFN_BUCKET=sample-bucket \
    CFN_PREFIX=sample-lambda
```

### デプロイ

```bash
make deploy
# カスタマイズ用
make deploy \
    PACKAGE_PATH=packaged.yaml \
    STACK_NAME=sample-stack
```


## Bringing to the next level

Here are a few ideas that you can use to get more acquainted as to how this overall process works:

* Create an additional API resource (e.g. /hello/{proxy+}) and return the name requested through this new path
* Update unit test to capture that
* Package & Deploy

Next, you can use the following resources to know more about beyond hello world samples and how others structure their Serverless applications:

* [AWS Serverless Application Repository](https://aws.amazon.com/serverless/serverlessrepo/)
* [Chalice Python Serverless framework](https://github.com/aws/chalice)
* Sample Python with 3rd party dependencies, pipenv and Makefile: ``sam init --location https://github.com/aws-samples/cookiecutter-aws-sam-python``
