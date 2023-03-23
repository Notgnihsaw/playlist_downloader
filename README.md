# Youtube Playlist Downloader

This is a short user guide for the download_playlist python script and the accompanying bash script, download_playlist_slurm.sh. 

The download_playlist_slurm.sh file is a batch file, which can be run directly from the command line on Discovery. To run this, you don't need to set up anaconda. Log into Discovery, go to the terminal, and use the following command:
`./download_playlist_slurm playlist_url download_path output_prefix`.

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

If you want to run the python program  on Discovery, follow this guide to set up anaconda: https://rc-docs.northeastern.edu/en/latest/software/conda.html. 
