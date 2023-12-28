# imap-mail-relay

## 概要

IMAPサーバーからメールを受信し、JSONに変換するAPIサーバーです。

## 使い方

Dockerイメージのビルド。

```bash
docker build -t imap-mail-relay .
```

Dockerコンテナの起動。

```bash
docker run -d --name mycontainer -p 8000:8000 imap-mail-relay
```
