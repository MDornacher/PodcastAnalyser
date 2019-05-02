import opml
from pyPodcastParser.Podcast import Podcast
import requests

outline = opml.parse('feed.opml')
f = open("output.txt", "w")

for shows in outline:
    podcast_url = shows.xmlUrl
    # print(podcast_url)

    response = requests.get(podcast_url)
    podcast = Podcast(response.content)

    print(podcast.title)
    f.write(podcast.title)
    #print(len(podcast.items), "episodes found!")

    for episode in podcast.items:
        f.write(str(episode.published_date) + "\t" + str(episode.title) + "\t" + str(episode.itunes_duration))

f.close()
