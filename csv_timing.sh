#!/bin/bash
#SBATCH --job-name=timecsvread
#SBATCH --partition=sixhour
#SBATCH --mail-type=ALL
#SBATCH --mail-user=e378m007@ku.edu
#SBATCH --time=0-06:00:00
#SBATCH --output=time_csv_read_%j.log
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=16gb

module load anaconda/4.10
module load python/3.7
conda activate bio-env

echo "running python"

# run python script

python /home/e378m007/scratch/trim_reads/csv_read_through.py