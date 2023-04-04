# Youtube Playlist Downloader

This is a short user guide for the download_playlist python script and the accompanying bash script, download_playlist_slurm.sh. 

The download_playlist_slurm.sh file is a batch file, which can be run directly from the command line on Discovery. To run this, you don't need to set up anaconda yourself. 
Log into Discovery, go to the terminal, and navigate to the folder where the playlist downloader package is stored. Use the following command to give the program permission to run:
`chmod a+x download_playlist_slurm`
Then, to run the program, use the following command: 
`./download_playlist_slurm playlist_url download_path output_prefix`.
Make sure to replace "playlist_url" with your playlist url, "download_path" with the location you want the mp3 files to go, and "output prefix" with the prefix you want to use for the files. Right now, all of the files will be named in a sequence (eg. "output_prefix1.mp3", "output_prefix2.mp3", etc). 

To run this using Python on your home computer (or on discovery), you need to install the following python packages:

Required python packages:
```
- pytube
- BeautifulSoup
- requests
- pandas
- moviepy
```

An easy way to do this is by running `pip3 install -t requirements.txt`, which installs the necessary python packages from the attached text file.

stock python packages:
```
- os
- sys
- re
- json
```

If you want to run the python program on Discovery, follow this guide to set up anaconda: https://rc-docs.northeastern.edu/en/latest/software/conda.html. 
