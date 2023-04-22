# ベースとなるイメージを指定
FROM python:3.9-slim-buster

# 作業ディレクトリを指定
WORKDIR /app

# 必要なファイルをコピー
COPY requirements.txt .

# 必要なライブラリをインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションファイルをコピー
COPY . .

# ポート80番を公開
EXPOSE 80

# アプリケーションを起動
CMD [ "python", "app.py" ]
