import json
import os
from pprint import pprint
import re
from functools import cmp_to_key

mj_filename = "master.json"
mj_content = None
mj_file = open(mj_filename, "r")
mj_content = mj_file.read()
mj_file.close()
mj = json.loads(mj_content)

target_audio = mj["audio"][2]
"""
0 = mp42, 255k
1 = mp42, 128k
2 = mp42, 64k
3 = dash, 127k
4 = dash, 75k
"""

audio_dirname  = "%s_audio_%s" % (mj["clip_id"].split("-")[0], target_audio["id"])
audio_filename = "%s_audio_%s.mp4" % (mj["clip_id"].split("-")[0], target_audio["id"])

segments = os.listdir(audio_dirname)

pattern = r'segment-(\d+).m4s'
def get_segment_index(segment):
    matches = re.findall(pattern, segment)
    if len(matches) == 0:
        return None
    else:
        return int(matches[0])
def segment_cmp(a, b):
    a_segment_index = get_segment_index(a)
    b_segment_index = get_segment_index(b)
    if isinstance(a_segment_index, int) and isinstance(b_segment_index, int):
        return a_segment_index - b_segment_index
    if a_segment_index is None or b_segment_index is None:
        if a < b:
            return -1
        elif a > b:
            return 1
        return 0

segments = sorted(segments, key=cmp_to_key(segment_cmp))

audio_file = open(audio_filename, "wb")
for segment in segments:
    print(segment)
    with open(audio_dirname +"/"+ segment, mode='rb') as file:
        audio_file.write(file.read())
audio_file.close()

input("\nDONE!")