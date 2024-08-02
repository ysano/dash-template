FROM python:3.12-slim

# 非rootユーザーを作成
RUN useradd -m -s /bin/bash vscode

# gitをインストール
RUN apt-get update && apt-get install -y git && apt-get clean && rm -rf /var/lib/apt/lists/*


# 作業ディレクトリを設定
WORKDIR /app

# 依存関係をコピーしてインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコピー
COPY . .

# 所有権を非rootユーザーに変更
RUN chown -R vscode:vscode /app

# 環境変数を設定
ENV PORT=8080

# 非rootユーザーに切り替え
USER vscode

# アプリケーションを実行
CMD gunicorn -b 0.0.0.0:$PORT app:server