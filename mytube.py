import sys
import yt_dlp

def download_video(video_url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,  # Ensure only one video is downloaded, not a playlist
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"Video downloaded successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def download_audio(video_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'extractaudio': True,
        'audioformat': 'mp3',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"Audio downloaded successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python mytube.py [video|audio] [YouTube URL]")
        sys.exit(1)

    format_type = sys.argv[1]
    video_url = sys.argv[2]

    print(f"Format type: {format_type}")
    print(f"Video URL: {video_url}")

    if format_type.lower() == 'video':
        download_video(video_url)
    elif format_type.lower() == 'audio':
        download_audio(video_url)
    else:
        print("Invalid format. Use 'video' to download video or 'audio' to download audio.")
