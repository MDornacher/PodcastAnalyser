import argparse
import datetime
import opml
import requests
import matplotlib.pyplot as plt
import mplcursors
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
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--opml", help="Path to opml file")
    ap.add_argument("-w", "--weeks", help="Number of weeks to average")
    args = vars(ap.parse_args())

    if args["opml"] and args["weeks"]:
        outline = opml.parse(args["opml"])
        week_margin = float(args["weeks"])
    else:
        print("The following arguments are required: -i/--opml, -w/--weeks")
        exit()

    weekday_time_total = [0] * 7
    weekday_order = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}
    x = range(len(weekday_order))

    podcast_list = []
    for shows in outline:
        podcast_url = shows.xmlUrl
        response = requests.get(podcast_url)
        podcast = Podcast(response.content)

        podcast_list.append(MyPodcast(podcast.title))
        print(podcast.title)

        weekday_time = [0] * 7

        for episode in podcast.items:
            # print(episode.title.encode("utf-8"))
            duration = episode.itunes_duration
            if duration is not None:
                weekday, day, month, year, *_ = episode.published_date.replace(",", "").split()
                today = datetime.date.today()
                margin = datetime.timedelta(weeks=week_margin)
                date = datetime.datetime.strptime(day + month + year, "%d%b%Y").date()

                if not today - margin <= date <= today:
                    continue

                duration = get_duration_in_seconds(duration)

                weekday_time[weekday_order[weekday]] += duration / (week_margin * 60)
                weekday_time_total[weekday_order[weekday]] += duration / (week_margin * 60)

                new_episode = MyEpisode(weekday, day, month, year, str(duration))
                podcast_list[-1].add_episode(new_episode)
        bottom_margin = [weekday_time_total[i] - weekday_time[i] for i in range(len(weekday_time))]
        plt.bar(x, weekday_time, align="center", bottom=bottom_margin, label=podcast.title)
    plt.xticks(x, weekday_order.keys())
    plt.hlines(y=range(0, int(max(weekday_time_total)), 60), xmin=-0.5, xmax=6.5, color="k", LineStyle = ':', alpha=0.3)
    plt.title("Weekly Podcast Consumption\nAverage Total per Week: %d min, per Day: %d min" % (sum(weekday_time_total), sum(weekday_time_total) / 7.))
    # TODO: make labels on hover appear
    # mplcursors.cursor(hover=True)

    plt.show()
