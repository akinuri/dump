import subprocess

audio_file = "74595329_audio_48eb6c54.mp4"
processed_audio_file = "74595329_audio_48eb6c54_p.mp4"

subprocess.call([
    "ffmpeg",
    "-i",
    audio_file,
    "-c",
    "copy",
    processed_audio_file,
])

input("\nDONE!")