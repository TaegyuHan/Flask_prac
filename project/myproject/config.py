import os

# 프로젝트의 루트 디렉터리
BASE_DIR = os.path.dirname(__file__)

# 데이터 베이스 접속 주소
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))

# 이벤트를 처리하는 옵션
SQLALCHEMY_TRACK_MODIFICATIONS = False

