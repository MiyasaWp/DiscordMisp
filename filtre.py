class EventFilter:
    def __init__(self, config):
        self.allowed_tlp = config.filters.get("tlp", ["white", "green"])
        self.min_threat = config.filters.get("min_threat_level", 4)
        self.excluded_tags = config.filters.get("tags_exclude", [])

    def passes(self, event) -> bool:
        # (1=High, 2=Medium, 3=Low, 4=Undefined)
        if int(event.threat_level_id) > self.min_threat:
            return False

        # Filtre par TLP
        event_tags = [t.name.lower() for t in (event.tags or [])]
        tlp_tags = [t for t in event_tags if t.startswith("tlp:")]
        if tlp_tags:
            tlp_value = tlp_tags[0].replace("tlp:", "")
            if tlp_value not in self.allowed_tlp:
                return False

        # Filtre tags exclus
        for tag in self.excluded_tags:
            if tag.lower() in event_tags:
                return False

        return True