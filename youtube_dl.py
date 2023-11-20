import sys
from pytube import YouTube
from tqdm import tqdm

def download_youtube_video(url, path):
    try:
        print("Starting the download process...")
        yt = YouTube(url)

        print(f"Video Title: {yt.title}")
        video_stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()

        # Getting the size of the video
        filesize = video_stream.filesize

        # Define a custom function to handle on_progress
        def on_progress(stream, chunk, bytes_remaining):
            current = filesize - bytes_remaining
            progress.update(current - progress.n)

        yt.register_on_progress_callback(on_progress)

        # Adding a progress bar
        with tqdm(total=filesize, unit='B', unit_scale=True, unit_divisor=1024, desc=yt.title, ascii=True) as progress:
            video_stream.download(output_path=path)

        print(f"Downloaded: {yt.title} to {path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        download_youtube_video(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python youtube_dl.py [YouTube URL] [Download Path]")

