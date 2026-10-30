# Final Project Submission Answers

Repository: https://github.com/Ragi509/oaqjp-final-project-emb-ai

---

### Question 1 (URL - 1 pt)
**Task 1: Submit the public GitHub repository URL of README.md file, which contains the project name details.**

```
https://github.com/Ragi509/oaqjp-final-project-emb-ai/blob/main/README.md
```

---

### Question 2 (TEXT - 1 pt)
**Task 2: Activity 1: Copy and paste the code of the emotion_detection.py, saved in a file named 2a_emotion_detection.**

```python
import requests

def emotion_detector(text_to_analyze):
    """Send text to Watson NLP and return the raw response text."""
    url = (
        "https://sn-watson-emotion.labs.skills.network"
        "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, headers=headers, json=payload, timeout=30)
    return response.text
```

---

### Question 3 (TEXT - 1 pt)
**Task 2: Activity 2: Copy and paste the terminal output, saved in the file named 2b_application_creation.**

```
theia@theiadocker-ragi509:/home/project/final_project$ python3
Python 3.11.5 (main, Aug 28 2023, 14:18:21) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from emotion_detection import emotion_detector
>>> print(emotion_detector('I am really mad about this'))
{"emotionPredictions":[{"emotion":{"anger":0.6865231,"disgust":0.007629255,"fear":0.027092923,"joy":0.021008272,"sadness":0.063231364},"target":""}],"producerId":{"name":"Voting based Ensemble Predictor","version":"0.0.1"}}
>>> exit()
theia@theiadocker-ragi509:/home/project/final_project$ python3 test_emotion_detection.py
theia@theiadocker-ragi509:/home/project/final_project$ 
```

---

### Question 4 (TEXT - 1 pt)
**Task 3: Activity 1: Copy and paste the code of the emotion_detection.py file saved in a file named 3a_output_formatting.**

```python
import json
import requests

def emotion_detector(text_to_analyze):
    """Send text to Watson NLP and return parsed emotion scores dict."""
    url = (
        "https://sn-watson-emotion.labs.skills.network"
        "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, headers=headers, json=payload, timeout=30)
    formatted_response = json.loads(response.text)

    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(scores, key=scores.get)
    scores['dominant_emotion'] = dominant_emotion

    return scores
```

---

### Question 5 (TEXT - 1 pt)
**Task 3: Activity 2: Copy and paste the terminal output, saved in the file named 3b_formatted_output_test.**

```
theia@theiadocker-ragi509:/home/project/final_project$ python3
Python 3.11.5 (main, Aug 28 2023, 14:18:21) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from emotion_detection import emotion_detector
>>> print(emotion_detector('I am really mad about this'))
{'anger': 0.6865231, 'disgust': 0.007629255, 'fear': 0.027092923, 'joy': 0.021008272, 'sadness': 0.063231364, 'dominant_emotion': 'anger'}
>>> exit()
theia@theiadocker-ragi509:/home/project/final_project$ 
```

---

### Question 6 (URL - 1 pt)
**Task 4: Activity 1: Submit the public GitHub repository URL of the __init__.py file.**

```
https://github.com/Ragi509/oaqjp-final-project-emb-ai/blob/main/EmotionDetection/__init__.py
```

---

### Question 7 (TEXT - 1 pt)
**Task 4: Activity 2: Copy and paste the terminal output saved in the file named 4b_packaging_test.**

```
theia@theiadocker-ragi509:/home/project/final_project$ python3 -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am very angry'))"
{'anger': 0.7251846, 'disgust': 0.009412534, 'fear': 0.03152643, 'joy': 0.015298412, 'sadness': 0.057821438, 'dominant_emotion': 'anger'}
theia@theiadocker-ragi509:/home/project/final_project$ 
```

---

### Question 8 (TEXT - 1 pt)
**Task 5: Activity 1: Copy and paste the code of the test_emotion_detection.py file, saved in a file named 5a_unit_testing.**

```python
"""Unit tests for EmotionDetection package - Task 5."""

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for the emotion_detector function."""

    def test_joy(self):
        """Test that 'I am glad this happened' returns joy as dominant emotion."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        """Test that 'I am really mad about this' returns anger as dominant emotion."""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        """Test that disgusted statement returns disgust as dominant emotion."""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness(self):
        """Test that sad statement returns sadness as dominant emotion."""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear(self):
        """Test that afraid statement returns fear as dominant emotion."""
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()
```

---

### Question 9 (TEXT - 1 pt)
**Task 5: Activity 2: Copy and paste the terminal output saved in the file named 5b_unit_testing_result.**

```
theia@theiadocker-ragi509:/home/project/final_project$ python3 test_emotion_detection.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.842s

OK
theia@theiadocker-ragi509:/home/project/final_project$ 
```

---

### Question 10 (TEXT - 1 pt)
**Task 6: Activity 1: Copy and paste the code of the server.py file, saved in a file named 6a_server.**

```python
"""Flask web server for the Emotion Detector application."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def emotion_detector_route():
    """Detect emotions in the provided text and return a formatted response."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    response = emotion_detector(text_to_analyze)

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def index():
    """Render the main index page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

### Question 11 (UPLOAD - 1 pt)
**Task 6: Activity 2: Upload the image of the application deployment, saved as 6b_deployment_test.png.**

Upload file: `submission/6b_deployment_test.png`

---

### Question 12 (TEXT - 1 pt)
**Task 7: Activity 1: Copy and paste the code of the emotion_detection.py file, saved in a file named 7a_error_handling_function.**

```python
"""Emotion detection module using Watson NLP."""

import json
import requests


def emotion_detector(text_to_analyze):
    """Send text to Watson NLP and return parsed emotion scores dict.

    Returns a dict with keys: anger, disgust, fear, joy, sadness,
    dominant_emotion. dominant_emotion is the highest-scoring emotion.
    If the API returns status 400, all values are None.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network"
        "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, headers=headers, json=payload, timeout=30)

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    formatted_response = json.loads(response.text)
    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]

    scores = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
    }
    dominant_emotion = max(scores, key=scores.get)
    scores["dominant_emotion"] = dominant_emotion

    return scores
```

---

### Question 13 (TEXT - 1 pt)
**Task 7: Activity 2: Copy and paste the code of the server.py file, saved in a file named 7b_error_handling_server.**

```python
"""Flask web server for the Emotion Detector application."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def emotion_detector_route():
    """Detect emotions in the provided text and return a formatted response."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def index():
    """Render the main index page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

### Question 14 (UPLOAD - 1 pt)
**Task 7: Activity 3: Upload the application deployment output image that validates the error-handling functionality, saved as 7c_error_handling_interface.png.**

Upload file: `submission/7c_error_handling_interface.png`

---

### Question 15 (TEXT - 1 pt)
**Task 8: Activity 1: Copy and paste the code of the server.py file, saved in a file named 8a_server_modified.**

```python
"""Flask web server for the Emotion Detector application."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def emotion_detector_route():
    """Detect emotions in the provided text and return a formatted response."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def index():
    """Render the main index page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

### Question 16 (TEXT - 1 pt)
**Task 8: Activity 2: Copy and paste the terminal output, saved in the file named 8b_static_code_analysis.**

```
theia@theiadocker-ragi509:/home/project/final_project$ pylint server.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

theia@theiadocker-ragi509:/home/project/final_project$ 
```
