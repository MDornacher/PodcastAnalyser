import opml
import requests
from pyPodcastParser.Podcast import Podcast
from podcast_episodes import MyPodcast, MyEpisode


def get_duration_in_seconds(duration):
    duration_list = duration.split(":")
    hours = 0
    mins = 0
    secs = 0
    if len(duration_list) == 3:
        hours, mins, secs = duration_list
    elif len(duration_list) == 2:
        mins, secs = duration_list
    elif len(duration_list) == 1:
        secs = duration
    duration = int(hours) * 3600 + int(mins) * 60 + int(secs)

    return duration


if __name__ == "__main__":
    outline = opml.parse('feed.opml')
    f = open("output_filtered", "w")

    podcast_list = []
    for shows in outline:
        podcast_url = shows.xmlUrl
        response = requests.get(podcast_url)
        podcast = Podcast(response.content)

        podcast_list.append(MyPodcast(podcast.title))
        print(podcast.title)
        f.write("%s\n" % podcast.title)

        for episode in podcast.items:
            # print(episode.title.encode("utf-8"))
            duration = episode.itunes_duration
            if duration is not None:
                weekday, day, month, year, *_ = episode.published_date.replace(",", "").split()
                # TODO: convert date to calendar week number and use it as filter and norm factor
                if month not in ["Feb", "Mar", "Apr"]:
                    continue
                duration = get_duration_in_seconds(duration)

                new_episode = MyEpisode(weekday, day, month, year, str(duration))
                podcast_list[-1].add_episode(new_episode)
                f.write("%s\n" % duration)

# TODO: stacked histogram with mean week time
