import yt_dlp

# Function to download YouTube video using yt-dlp
def download_video(video_url):
    try:
        # Configure yt-dlp options
        ydl_opts = {
            'format': 'best',  # Download the best quality available
            'outtmpl': '%(title)s.%(ext)s'  # Save file as the video title
        }

        # Download the video using yt-dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video from: {video_url}")
            ydl.download([video_url])
            print("Download completed!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Get the YouTube video URL from the user
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)
