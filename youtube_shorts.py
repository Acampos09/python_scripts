import yt_dlp

# Function to download YouTube Shorts without requiring ffmpeg
def download_youtube_short(video_url):
    try:
        # yt-dlp options for downloading the best format without merging
        ydl_opts = {
            'format': 'best[ext=mp4]',  # Download the best format as MP4 without needing ffmpeg
            'outtmpl': '%(title)s.%(ext)s'  # Save the file using the title as the filename
        }

        # Start downloading the YouTube Short
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading YouTube Short from: {video_url}")
            ydl.download([video_url])
            print("Download completed!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Prompt the user to enter the YouTube Short URL
    video_url = input("Enter the YouTube Short URL: ")
    download_youtube_short(video_url)
