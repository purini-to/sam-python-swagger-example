from test.support import EnvironmentVarGuard


def setup_env(clazz):
    clazz.env = EnvironmentVarGuard()
    clazz.env.set('PET_NAME', 'tiger')
    clazz.env.set('AWS_ACCESS_KEY_ID', '<your access key id>')
    clazz.env.set('AWS_SECRET_ACCESS_KEY',
                  '<your secret key>')
    clazz.env.set('AWS_DEFAULT_REGION', 'ap-northeast-1')
