# Podcast Analyser

Calculate and plot daily podcast duration of feed.

## Packages

```
argparse
datetime
matplotlib
opml
pyPodcastParser
requests
```

## Usage

Export your subscriptions as opml file from your podcast app and run:
```
python podaliser.py -i [opml file] -w [int of weeks to averge]
```

## Output

Example output with 
```
python podaliser.py -i example/feed.opml -w 4
```

![Example output](example/figure.png?raw=true "Example output")

## Known Problems

* For a higher number of podcasts in feed the plot gets increasingly unclear.
* Averaging over the entire specified interval is not the best solution for irregular scheduled podcasts.
* Podcasts with a high number of episodes increase the computation time, since the information of all episodes is retrieved before filtering.