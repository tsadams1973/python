from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry

import os
import sys

if 'CUSTOM_VISION_ENDPOINT' in os.environ:
    ENDPOINT = os.environ['CUSTOM_VISION_ENDPOINT']
else:
    print("\CUSTOM_VISION_ENDPOINT key missing.")
    sys.exit()

if 'TRAINING_KEY' in os.environ:
    training_key = os.environ['TRAINING_KEY']
else:
    print("\TRAINING_KEY key missing.")
    sys.exit()

if 'PREDICTION_KEY' in os.environ:
    prediction_key = os.environ['PREDICTION_KEY']
else:
    print("\PREDICTION_KEY key missing.")
    sys.exit()

if 'PREDICTION_RES_ID' in os.environ:
    prediction_resource_id = os.environ['PREDICTION_RES_ID']
else:
    print("\PREDICTION_RES_ID key missing.")
    sys.exit()



print(ENDPOINT) 
print(training_key)
print(prediction_key)
print(prediction_resource_id)

publish_iteration_name = "classifyModel"

trainer = CustomVisionTrainingClient(training_key, endpoint=ENDPOINT)

# Create a new project
print ("Creating project...")
#project = trainer.create_project("My New Project")