import sys
import requests
import json
import os
import base64

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

master_json_url = "https://10vod-adaptive.akamaized.net/exp=1650461792~acl=%2F74595329-11a7-4673-9a2a-4d4842f8eb89%2F%2A~hmac=3959646d1a911b3ab3d96037a2e8d2dcc2ef4b1522d3dbcf148971e8166d97ad/74595329-11a7-4673-9a2a-4d4842f8eb89/sep/video/36f891d2,48eb6c54,22a5b384,e7f0c05b,be7925bd/audio/3befbd40,8bb0aa93/master.json?query_string_ranges=1&base64_init=1"
audio_base_url = master_json_url.split("/sep/video/")[0] +"/"+ target_audio["base_url"].replace("../", "")
audio_dirname  = "%s_audio_%s" % (mj["clip_id"].split("-")[0], target_audio["id"])

os.mkdir(audio_dirname)
file_init = open(audio_dirname + "/init.m4s", "wb")
file_init.write(base64.b64decode(target_audio["init_segment"]))
file_init.close()

for audio_segment in target_audio["segments"]:
    audio_segment_url = audio_base_url + audio_segment["url"]
    print(audio_segment_url)
    segment_response = requests.get(audio_segment_url, stream=True)
    if segment_response.status_code != 200:
        print("\nSomething went wrong.\n")
        print(segment_response)
        input(EXIT_MSG)
        sys.exit()
    audio_segment = open(audio_dirname +"/"+ audio_segment["url"], "wb")
    for chunk in segment_response:
        audio_segment.write(chunk)
    audio_segment.close()

input("\nDONE!")