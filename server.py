"""This is a module  doc string"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_function():
    '''This is a function doc string'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is not  None:
        output_string = f"""For the given statement, the system response is 'anger':
                        {response['anger']} 'disgust': {response['disgust']},'fear':
                        {response['fear']}, 'joy': {response['joy']}, 'sadness': 
                        {response['sadness']}. The dominant emotion is 
                        {response['dominant_emotion']}."""
        return output_string
    return "Invalid text! Please try again!"

@app.route("/")
def render_index_page():
    '''This is a function doc string'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
