# finction for read the folders and imgs
# then the function will store it in a set and return the set
# the set will pass to the hash method
# the hash method will hash all images and store it in a set
# the set is returned and passed it to compare method
# the compare method will check in a specific method is
import os
from pathlib import Path
import hashlib as hl



#Return all images in the folder
def get_all_images_from_path(path):
    all_images = set()
    for image in Path(path).rglob("*"):
        if image.is_file() and image.suffix.lower() in [".jpg", ".jpeg",".png",".webp"]:
            all_images.add(str(image))
    return all_images

#Return the hash for all images in dataset
def hash_all_images(set_of_images):
    hashed_images = {}

    for single_image in set_of_images:
        hash_algo = hl.md5()
        with open(single_image, "rb") as f:
            while chunk := f.read(8192):
                hash_algo.update(chunk)
            the_hashed_image = hash_algo.hexdigest()
            hashed_images[the_hashed_image] = single_image
    return hashed_images

#Compare
def filter_dataset(new_dataset,old_dataset):
    resultsOfFilter = []
    the_duplicated_images_in_new_dataset = set()
    the_duplicated_images_in_old_dataset = set()
    for single_image in new_dataset.keys():
        if single_image in old_dataset.keys():
            the_duplicated_images_in_new_dataset.add(new_dataset[single_image])
            the_duplicated_images_in_old_dataset.add(old_dataset[single_image])
            resultsOfFilter.append(f"{new_dataset[single_image]} -> {old_dataset[single_image]}")
    return resultsOfFilter





#The folder / dataset you want to remove redundancy from , before add it to your main dataset
target_disease = r"C:\Users\aseel\Downloads\targetData"

#Your main dataset / Folder
the_whole_diseases=r"C:\Users\aseel\Downloads\mainData"


target_disease = get_all_images_from_path(target_disease)
target_disease = hash_all_images(target_disease)

the_whole_diseases = get_all_images_from_path(the_whole_diseases)
the_whole_diseases = hash_all_images(the_whole_diseases)

e_results = filter_dataset(target_disease,the_whole_diseases)
print(*e_results, sep="\n")

















