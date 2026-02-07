from yt_dlp import YoutubeDL

VIDEO_URL = "https://www.youtube.com/watch?v=VIDEO_ID"

ydl_opts = {
    # Best video up to 1080p + best audio
    "format": "bestvideo[height<=1080]+bestaudio/best[height<=1080]",

    # Merge into MP4
    "merge_output_format": "mp4",

    # Output folder & filename
    "outtmpl": "downloads/%(title)s.%(ext)s",

    # Reliability
    "retries": 10,
    "fragment_retries": 10,

    # Metadata
    "addmetadata": True,
    "embedthumbnail": True,

    # Cleaner logs
    "quiet": False,
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([VIDEO_URL])
