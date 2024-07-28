import requests 
import json

def emotion_detector(text_to_analyse):  
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    myobj = { "raw_document": { "text": text_to_analyse } } 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    response = requests.post(url, json = myobj, headers=header) 
    if response.status_code == 200:
        text_response = response.text  
        formatted_response = json.loads(text_response)
        json_emotion = formatted_response['emotionPredictions'][0]['emotion']
        temp_key = ""
        temp_value = 0
        for key in json_emotion:
            if json_emotion[key] >= temp_value:
                temp_value = json_emotion[key]
                temp_key = key
        json_emotion['dominant_emotion']= temp_key
        return json_emotion
    else:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
