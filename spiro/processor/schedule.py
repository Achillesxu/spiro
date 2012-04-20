import urlparse
from .base import Step

"""
Instead of handling 30X redirects as a HTTP case, we're handling them in the
response pipeline.
"""

class ScheduleUrls(Step):
    def __init__(self, settings, work_queue=None, **kwargs):
        """Initialzation"""
        self.work_queue = work_queue

    def process(self, task, callback=None, **kwargs):
        for url in task.links:
            self.work_queue.add(url)

        callback((Step.CONTINUE, task))
