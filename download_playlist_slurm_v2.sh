#!/bin/bash
#SBATCH --nodes=1
#SBATCH --time=8:00:00
#SBATCH --job-name=playlist_downloader
#SBATCH --partition=short

# Load in Anaconda Modules

module load anaconda3/2022.01

echo "Creating Anaconda module and downloading packages";

source activate peterb2023 

echo "Running Playlist Extractor";

# Run the Script
python3 download_playlist.py $1 $2 $3

echo "Shutting down Anaconda module";
# shutdown sequence (anaconda)
conda deactivate 

# TODO: parallelize this!
