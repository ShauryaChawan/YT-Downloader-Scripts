import sys
from pathlib import Path
from yt_dlp import YoutubeDL

# ----------------------------
# CONFIGURATION
# ----------------------------

PLAYLIST_URL = "https://music.youtube.com/playlist?list=PLTnEVrWxPf0TWqaOP_2zOPX5arXjlZ0J1"

# Default download directory
DEFAULT_DOWNLOAD_DIR = "E:\\Music"


# ----------------------------
# OPTIONAL CLI ARGUMENT
# Usage:
# python download_music_playlist.py D:/Music
# ----------------------------

if len(sys.argv) > 1:
    download_root = Path(sys.argv[1])
else:
    download_root = Path(DEFAULT_DOWNLOAD_DIR)

download_root.mkdir(parents=True, exist_ok=True)

# ----------------------------
# YT-DLP OPTIONS
# ----------------------------

ydl_opts = {
    # Best available audio
    "format": "bestaudio/best",

    # Output structure with custom root
    "outtmpl": str(download_root / "%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s"),

    # Playlist handling
    "yesplaylist": True,
    "ignoreerrors": True,

    # Convert to MP3
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        },
        {
            "key": "EmbedThumbnail",
        },
        {
            "key": "FFmpegMetadata",
        },
    ],

    # Performance & reliability
    "concurrent_fragment_downloads": 5,
    "retries": 10,
    "fragment_retries": 10,
}

# ----------------------------
# DOWNLOAD
# ----------------------------

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([PLAYLIST_URL])

print(f"\n✅ Download complete! Saved to: {download_root.resolve()}")
