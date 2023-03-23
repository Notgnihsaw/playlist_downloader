#!/bin/bash
#SBATCH --nodes=1
#SBATCH --time=8:00:00
#SBATCH --job-name=playlist_downloader
#SBATCH --partition=short

# Load in Anaconda Modules

module load anaconda3/2022.01

echo "Creating Anaconda module and downloading packages";

conda create -n temp_playlist_download python=3.7 anaconda -y
source activate temp_playlist_download 
conda install -n temp_playlist_download -c conda-forge pytube -y
conda install -n temp_playlist_download BeautifulSoup -y
conda install -n temp_playlist_download requests -y
conda install -n temp_playlist_download -c conda-forge pandas -y 
conda install -n temp_playlist_download -c conda-forge pytube -y

echo "Running Playlist Extractor";

# Run the Script
python3 download_playlist.py $1 $2 $3

echo "Shutting down Anaconda module";
# shutdown sequence (anaconda)
conda deactivate 
conda remove -n temp_playlist_download --all

# TODO: parallelize this!