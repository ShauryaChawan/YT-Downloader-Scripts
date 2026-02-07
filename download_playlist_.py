from yt_dlp import YoutubeDL

PLAYLIST_URL = "https://www.youtube.com/playlist?list=PLmKwZ83G-3jV9CNHaypDoluIKlKj51P_4"

ydl_opts = {
    # Best video up to 1080p + best audio
    "format": "bestvideo[height<=1080]+bestaudio/best[height<=1080]",

    # Merge video & audio into MP4
    "merge_output_format": "mp4",

    # Output folder & filename
    "outtmpl": "downloads/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s",

    # Playlist options
    "yesplaylist": True,
    "ignoreerrors": True,

    # Performance & stability
    "concurrent_fragment_downloads": 5,
    "retries": 10,
    "fragment_retries": 10,

    # Metadata
    "addmetadata": True,
    "embedthumbnail": True,
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([PLAYLIST_URL])
