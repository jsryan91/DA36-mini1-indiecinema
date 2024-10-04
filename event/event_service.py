from event.event_repo import *

class EventService:
    def __init__(self):
        self.event_repo=EventRepo()

    def get_event_list(self):
        return self.event_repo.get_event_list()

    def get_event_by_title(self, title):
        return self.event_repo.get_event_by_title(title)

