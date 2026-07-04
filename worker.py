from redis import Redis
from rq import Worker, Queue, Connection
from config import settings
import os

try:
    from prometheus_client import start_http_server
except Exception:
    start_http_server = None


def run_worker():
    port = int(os.getenv("WORKER_METRICS_PORT", "8001"))
    if start_http_server:
        try:
            start_http_server(port)
        except Exception:
            pass

    redis_conn = Redis.from_url(settings.redis_url)
    with Connection(redis_conn):
        worker = Worker(Queue("default"))
        worker.work()


if __name__ == "__main__":
    run_worker()
