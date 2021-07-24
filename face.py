from deepface import DeepFace
import keras
def getCharacteristics():
    obj = DeepFace.analyze(img_path = "test.jpg", actions = ['age', 'gender', 'race', 'emotion'])
    return obj