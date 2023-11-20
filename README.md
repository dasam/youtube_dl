# YouTube Video Downloader

This Python script allows users to download videos from YouTube directly to their local storage in MP4 format. It uses the `pytube` library and features a progress bar via the `tqdm` library for a clear, visual download progress indication.

## Features

- Download YouTube videos in MP4 format.
- Progress bar for download status.
- Command-line interface for easy use.

## Installation

Before running the script, ensure you have Python installed on your system. This script is tested with Python 3.11.4.

### Dependencies

- `pytube`: Used to fetch and download videos from YouTube.
- `tqdm`: Provides a progress bar during the download.

Install the required packages using pip:

```bash
pip install pytube tqdm
```

### Usage
To use the script, run it from the command line with the URL of the YouTube video and the desired download path as arguments.

```bash
python youtube_dl.py [YouTube URL] [Download Path]
```
For example:
```bash
python youtube_dl.py https://www.youtube.com/watch?v=jUaZ7LxvMsY C:\Downloads
```

### Troubleshooting
If you encounter any issues, ensure that:

- Python and the required libraries (pytube and tqdm) are correctly installed.
- The YouTube URL and the download path are correctly specified.
- You have write permissions to the specified download path.

### Contributing
Contributions to this project are welcome! Please feel free to fork the repository, make changes, and submit a pull request.

### License
This project is released under the MIT License. See the LICENSE file for more details.
