
class EventManager():

    def __init__(self):

        self.suscribers = {}

    def suscribe(self, event_type: str, func: callable):
        if event_type not in self.suscribers:
            self.suscribers[event_type].append(func)

    def broadcast_event(self, event_type: str, **kwargs):
        if event_type not in self.suscribers:
            return
        for func in self.suscribers[event_type]:
            func(**kwargs)
