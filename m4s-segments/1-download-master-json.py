import requests
import json

master_json_url = "https://10vod-adaptive.akamaized.net/exp=1650463490~acl=%2F74595329-11a7-4673-9a2a-4d4842f8eb89%2F%2A~hmac=1188bba8adc8dd948beeee283cfc127d3554840078b4bbf0394e08ddcc789241/74595329-11a7-4673-9a2a-4d4842f8eb89/sep/video/36f891d2,48eb6c54,22a5b384,e7f0c05b,be7925bd/audio/3befbd40,8bb0aa93/master.json?query_string_ranges=1&base64_init=1"
master_json_url_response = requests.get(master_json_url)
master_json = master_json_url_response.json()

master_json_filename = "master.json"

file = open(master_json_filename, "w")
file.write(json.dumps(master_json, indent = 4))
file.close()

input("DONE!")