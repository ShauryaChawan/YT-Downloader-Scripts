import subprocess
from pathlib import Path

# Root directory containing .webm files
ROOT_DIR = Path("downloads")

# Set to False if you want to KEEP original .webm files
DELETE_ORIGINAL = False


def convert_webm_to_mp4(webm_path: Path):
    mp4_path = webm_path.with_suffix(".mp4")

    if mp4_path.exists():
        print(f"⏭️ Skipping (already exists): {mp4_path}")
        return

    print(f"🎬 Converting: {webm_path}")

    cmd = [
        "ffmpeg",
        "-y",                   # overwrite if needed
        "-i", str(webm_path),
        "-map", "0:v:0",
        "-map", "0:a?",
        "-c:v", "copy",         # no re-encode (fast)
        "-c:a", "aac",
        "-movflags", "+faststart",
        str(mp4_path),
    ]

    subprocess.run(cmd, check=True)


def main():
    webm_files = list(ROOT_DIR.rglob("*.webm"))

    if not webm_files:
        print("❌ No .webm files found.")
        return

    for webm_file in webm_files:
        try:
            convert_webm_to_mp4(webm_file)

            if DELETE_ORIGINAL:
                webm_file.unlink()
                print(f"🗑️ Deleted: {webm_file}")

        except subprocess.CalledProcessError:
            print(f"❌ Failed: {webm_file}")

    print("✅ Conversion complete.")


if __name__ == "__main__":
    main()
