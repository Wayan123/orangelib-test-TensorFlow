
from orangelib.model import OrangeClassifier

classifier = OrangeClassifier("orange_model.h5")

fruit_name, confidence = classifier.predict("jeruk.jpg")

print(" Fruit Name: ",fruit_name)
print("Prediction Confidence: ",confidence)