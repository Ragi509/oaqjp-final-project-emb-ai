"""Emotion detection module using Watson NLP."""

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

    data = response.json()
    emotions = (
        data.get("emotionPredictions", [{}])[0]
        .get("emotion", {})
    )
    anger = emotions.get("anger", 0)
    disgust = emotions.get("disgust", 0)
    fear = emotions.get("fear", 0)
    joy = emotions.get("joy", 0)
    sadness = emotions.get("sadness", 0)

    scores = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
    }
    dominant_emotion = max(scores, key=scores.get)

    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion,
    }
