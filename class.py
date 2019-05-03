
class Episode:
    def __init__(self, name, date, duration):
        self.title = name
        self.published_date = date
        self.itunes_duration = duration

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.__str__()


class Podcast:
    def __init__(self, name):
        self.title = name
        self.items = []

    def add_episode(self, episode):
        self.items.append(episode)


episode1 = Episode("HI1", "Thu", "40")
episode2 = Episode("HI2", "Thu", "40")
episode3 = Episode("HI3", "Thu", "40")
episode4 = Episode("HI4", "Thu", "40")
print(episode4)

podcast = Podcast("Hello Internet")
podcast.add_episode(episode1)
podcast.add_episode(episode2)
podcast.add_episode(episode3)
podcast.add_episode(episode4)
print(podcast.items)
