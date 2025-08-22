import requests  # Import the requests library to handle HTTP requests
import json


# Define a function named emotion detector that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyse):  
    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Sending a POST request to the emotion detector API
    response = requests.post(url, json=myobj, headers=header)
    
    # Extracting emotions from the response
    # Any emotion values will be None for any status code but 200
    result = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        }

    print (response.status_code)

    if response.status_code == 200:
        # Parsing the JSON response from the API
        formatted_response = json.loads(response.text)
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        # Returning a dictionary containing emotion detection results
        result = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
        }

    return result