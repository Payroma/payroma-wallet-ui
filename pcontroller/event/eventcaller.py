class EventCaller:
    def __init__(self):
        self.__listeners = []
        self.isStopped = False

    def notify(self, **kwargs):
        """Calling all listeners listening to this event"""

        if self.isStopped:
            return

        for listener in self.__listeners:
            try:
                listener(**kwargs)
            except RuntimeError:
                continue

    def listen(self, listener):
        """Add new listener"""

        if listener not in self.__listeners:
            self.__listeners.append(listener)

    def remove(self, listener=None):
        """Remove a listener already listening"""

        if listener:
            try:
                self.__listeners.remove(listener)
            except ValueError:
                pass
        else:
            self.__listeners.clear()
