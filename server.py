"""
Emotion Detector Server

This is a Flask-based server that analyzes emotions in the given text and returns the result.

Author: Your Name
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Analyze emotions in the given text and return the result.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid text! Please try again!"

    dominant_emotion = response['dominant_emotion']
    score = response[dominant_emotion]
    label = dominant_emotion.capitalize()
    score_formatted = f"{score:.2%}"
    result_text = (
        f"For the given statement, the system response is {label}: {score_formatted}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return result_text

@app.route("/")
def render_index_page():
    """
    Render the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
