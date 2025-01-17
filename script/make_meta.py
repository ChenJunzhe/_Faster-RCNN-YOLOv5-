import argparse
import os
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('-t', type=int, default=20, help="number of test data")

args = parser.parse_args()

ROOT_DIR = "C:\\Users\\ChenJunzhe\\Desktop\\cs1.6\\cstrike-detection-main\\dataset"
IMAGE_DIR = os.path.join(ROOT_DIR, "images")
LABEL_DIR = os.path.join(ROOT_DIR, "labels")
EXCLUDE_FILE = ["classes.txt"]
TEST_NUM = args.t

all_images = os.listdir(IMAGE_DIR)

if TEST_NUM > len(all_images):
    raise ValueError("size of test dataset must be smaller than total size {}".format(len(all_images)))

indice = np.arange(len(all_images))
print(len(all_images))
np.random.shuffle(indice)
train_image_fp = open(os.path.join(ROOT_DIR, "traindata.txt"), "w", encoding="utf-8")
test_image_fp = open(os.path.join(ROOT_DIR, "testdata.txt"), "w", encoding="utf-8")

for i in indice[:-TEST_NUM]:
    abspath = os.path.abspath(os.path.join(IMAGE_DIR, all_images[i]))
    train_image_fp.write(abspath)
    train_image_fp.write("\n")

for i in indice[-TEST_NUM:]:
    abspath = os.path.abspath(os.path.join(IMAGE_DIR, all_images[i]))
    test_image_fp.write(abspath)
    test_image_fp.write("\n")

train_image_fp.close()
test_image_fp.close()