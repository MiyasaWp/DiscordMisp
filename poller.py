from pymisp import PyMISP
from datetime import datetime, timedelta

class MISPPoller:
    def __init__(self, config):
        self.misp = PyMISP(config.misp_url, config.misp_key, ssl=False)
        self.last_check = datetime.utcnow() - timedelta(minutes=5)

    def fetch_new_events(self):
        #Recup les evenements MISP depuis le dernier check
        events = self.misp.search(
            controller='events',
            timestamp=int(self.last_check.timestamp()),
            published=True,
            pythonify=True
        )
        self.last_check = datetime.utcnow()
        return events

    def get_event_by_id(self, event_id):
        return self.misp.get_event(event_id, pythonify=True)