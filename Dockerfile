# ベースイメージの選択
FROM python:3.9

# 作業ディレクトリの設定
WORKDIR /app

# 依存関係ファイルのコピー
COPY requirements.txt .

# 依存関係のインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションファイルのコピー
COPY . .

# コンテナがリッスンするポート番号を指定
EXPOSE 8000

# アプリケーションの実行
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
