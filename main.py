from util import build_dictionary
from deepdiff import DeepDiff
import json

url = 'https://en.wikipedia.org/wiki/List_of_most-streamed_songs_on_Spotify'

build_dictionary(url)

with open('3_27_2022.json', 'r') as file:
    last_week = json.load(file)
with open('4_5_2022.json', 'r') as file:
    this_week = json.load(file)

diff = DeepDiff(last_week, this_week)

with open('diff.json', 'w') as file:
    json.dump(diff, file, indent=4)