# Gunicorn configuration file
import multiprocessing

# 同時実行ワーカー数
workers = multiprocessing.cpu_count() * 2 + 1

# ワーカークラスの指定
worker_class = "sync"

# バインドするアドレスとポート
bind = "0.0.0.0:5050"


# タイムアウトの設定
timeout = 60
