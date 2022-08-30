from __future__ import absolute_import
from celery import shared_task


@shared_task
def test(param):
    return 'The tasks executed with the following parameter: "%s" ' % param
