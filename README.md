



1. git cloneする

    ```jsx
    git clone https://github.com/Akiyoshi-Yagi/susrepo.git
    ```

2. requirements.txtでライブラリ•モジュールインストール

    ```jsx
    $ pip install -r requirements.txt
    ```

3. マイグレーション

    ```
    python manage.py migrate
    ```

4. データをデータベースに格納しちゃう

    ```
    python manage.py import_companies
    ```

5. 環境変数ファイル .env の作成（極秘🥺）

    manage.pyと同じ階層に .env　を作成する

    ```
    AUTH0_CLIENT_ID=6PIGOOILO58I9Qa9Si44gf5p0QUOVvcp
    AUTH0_CLIENT_SECRET=YOK_gVAzalQOEw4RoWV2D52c2USzkznRmfejmVr_ZQ3JQ_WgoX8422jp8lT67hyQ
    AUTH0_DOMAIN=dev-rs1okhla1dki4gnk.us.auth0.com

    OPENAI_API_KEY=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

    DEBUG=False
    ALLOWED_HOSTS=127.0.0.1, localhost
    DATABASE_URL=sqlite:///db.sqlite3
    ```

6. python manage.py runserver　でdjangoプロジェクトを立ち上げる



for 小原
- source .venv/bin/activateで仮想環境を起動


- python-dotenv
-django
- django-environを追加した
- authlib
- requests


pythonはpython3だと上手くいくことあり
DBっぽいエラーは
python manage.py migrate
python manage.py import_companies
をやり直す


DB変更したら、前のやつ消去

obara-taichi@g.ecc.u-tokyo.ac.jp
passは
1234aaa#



## 知りたいこと
- 有報情報取得の方法
- DB追加
-
