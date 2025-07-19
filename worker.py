from celery import Celery
from app.pipeline import run_pipeline

celery_app = Celery("crew_pipeline", broker="redis://localhost:6379/0")

@celery_app.task
def process_topic(topic):
    run_pipeline(topic)