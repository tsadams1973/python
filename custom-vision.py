from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry

import os
import sys

if 'CUSTOM_VISION_ENDPOINT' in os.environ:
    ENDPOINT = os.environ['CUSTOM_VISION_ENDPOINT']
else:
    print("\nCUSTOM_VISION_ENDPOINT key missing.")
    sys.exit()

if 'TRAINING_KEY' in os.environ:
    training_key = os.environ['TRAINING_KEY']
else:
    print("\nTRAINING_KEY key missing.")
    sys.exit()

if 'PREDICTION_KEY' in os.environ:
    prediction_key = os.environ['PREDICTION_KEY']
else:
    print("\nPREDICTION_KEY key missing.")
    sys.exit()

if 'PREDICTION_RES_ID' in os.environ:
    prediction_resource_id = os.environ['PREDICTION_RES_ID']
else:
    print("\nPREDICTION_RES_ID key missing.")
    sys.exit()

if 'IMAGE_PATH' in os.environ:
    IMAGE_URL = os.environ['IMAGE_PATH']
else:
    print("\IMAGE_PATH missing.")
    sys.exit()

'''
# Just check the environment variables are set
print(ENDPOINT) 
print(training_key)
print(prediction_key)
print(prediction_resource_id)
print(IMAGE_URL)
'''

publish_iteration_name = "classifyModel"

trainer = CustomVisionTrainingClient(training_key, endpoint=ENDPOINT)

# Create a new project
print ("Creating project...")
project = trainer.create_project("test-project-qs")

# Make two tags in the new project
hemlock_tag = trainer.create_tag(project.id, "Hemlock")
cherry_tag = trainer.create_tag(project.id, "Japanese Cherry")

#added the path to the environment variables in conda env-01
base_image_url = IMAGE_URL

print("Adding images...")

image_list = []

for image_num in range(1, 11):
    file_name = "hemlock_{}.jpg".format(image_num)
    with open(base_image_url + "images/Hemlock/" + file_name, "rb") as image_contents:
        image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), tag_ids=[hemlock_tag.id]))

for image_num in range(1, 11):
    file_name = "japanese_cherry_{}.jpg".format(image_num)
    with open(base_image_url + "images/Japanese Cherry/" + file_name, "rb") as image_contents:
        image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), tag_ids=[cherry_tag.id]))

upload_result = trainer.create_images_from_files(project.id, images=image_list)
if not upload_result.is_batch_successful:
    print("Image batch upload failed.")
    for image in upload_result.images:
        print("Image status: ", image.status)
    exit(-1)

import time

print ("Training...")
iteration = trainer.train_project(project.id)
while (iteration.status != "Completed"):
    iteration = trainer.get_iteration(project.id, iteration.id)
    print ("Training status: " + iteration.status)
    time.sleep(1)

# The iteration is now trained. Publish it to the project endpoint
trainer.publish_iteration(project.id, iteration.id, publish_iteration_name, prediction_resource_id)
print ("Done!")

from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient

# Now there is a trained endpoint that can be used to make a prediction
predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)

with open(base_image_url + "images/Test/test_image.jpg", "rb") as image_contents:
    results = predictor.classify_image(
        project.id, publish_iteration_name, image_contents.read())

    # Display the results.
    for prediction in results.predictions:
        print("\t" + prediction.tag_name +
              ": {0:.2f}%".format(prediction.probability * 100))
