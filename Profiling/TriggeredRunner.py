""" python-sandbox :: TriggeredRunner

Description:
    Class for encapsulating a function to wait as a background thread until start_event is set, then run and until stop_event.
    Intended usage is for functions that have no intended fixed finish time.

Author:
    marcusljx

Created:
    2016-09-05
"""
import threading


class TriggeredRunner(threading.Thread):
    def __init__(self, func, args, start_event=None, stop_event=None, interval=1.0):
        assert isinstance(stop_event, threading.Event)
        super().__init__()
        self._start_event = start_event
        self._stop_event = stop_event
        self._interval = interval

        def __f():
            return func(*args)

        self.__exec = __f

    def run_once(self):
        return self.__exec()

    def run(self):
        while self._start_event and not self._start_event.is_set():
            pass

        while self._stop_event or not self._stop_event.is_set():
            self.run_once()
