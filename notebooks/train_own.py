from AxonDeepSeg.data_management.dataset_building import *
from AxonDeepSeg.ads_utils import download_data
import os, shutil
from pathlib import Path

data_split_path = Path("./split")
data_patched_path = Path("./patched")
data_training_path = Path("./training")

'''
# If dataset building folders already exist, remove them.
if data_split_path.exists():
    shutil.rmtree(data_split_path)
if data_patched_path.exists():
    shutil.rmtree(data_patched_path)
if data_training_path.exists():
    shutil.rmtree(data_training_path)
 '''   
downloaded_data = Path("./SEM_dataset")
# Set seed (changing value will change how the dataset is split)
seed = 2019

# Set dataset split fraction [Train, Validation]
split = [0.8, 0.2]

# Split data into training and validation datasets 
#split_data(downloaded_data, data_split_path, seed=seed, split=split)


# Define the paths for the training samples
path_raw_data_train = data_split_path / 'Train'
path_patched_data_train = data_patched_path / 'Train'

# Define the paths for the validation samples
path_raw_data_validation = data_split_path / 'Validation'
path_patched_data_validation = data_patched_path / 'Validation'

patch_size = 512
general_pixel_size = 0.0476

# Split the *Train* dataset into patches
raw_img_to_patches(path_raw_data_train, path_patched_data_train, thresh_indices = [0, 0.2, 0.8], patch_size=patch_size, resampling_resolution=general_pixel_size)

# Split the *Validation* dataset into patches
raw_img_to_patches(path_raw_data_validation, path_patched_data_validation, thresh_indices = [0, 0.2, 0.8], patch_size=patch_size, resampling_resolution=general_pixel_size)


# Path of the final training dataset
path_final_dataset_train = data_training_path / 'Train'

# Path of the final validation dataset
path_final_dataset_validation = data_training_path / 'Validation'


# Regroup all training patches
patched_to_dataset(path_patched_data_train, path_final_dataset_train, type_='unique', random_seed=2017)

# Regroup all validation patches
patched_to_dataset(path_patched_data_validation, path_final_dataset_validation, type_='unique', random_seed=2017)

# Remove intermediate dataset building folders

if downloaded_data.exists():
    shutil.rmtree(downloaded_data)
if data_split_path.exists():
    shutil.rmtree(data_split_path)
if data_patched_path.exists():
    shutil.rmtree(data_patched_path)
