class MyEpisode:
    def __init__(self, weekday, day, month, year, duration):
        self.weekday = weekday
        self.day = day
        self.month = month
        self.year = year
        self.duration = duration


class MyPodcast:
    def __init__(self, title):
        self.title = title
        self.episodes = []

    def add_episode(self, episode):
        self.episodes.append(episode)
