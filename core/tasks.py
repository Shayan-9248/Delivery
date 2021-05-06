from bucket import bucket
from celery import shared_task


def get_objects_list_task():
    return bucket.get_objects


@shared_task
def download_object_task(key):
    return bucket.download_object


@shared_task
def delete_object_task(key):
    return bucket.delete_object