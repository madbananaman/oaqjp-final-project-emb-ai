import requests
from icecream import ic


def emotion_detector(text_to_analyze: str):
    """
    URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input json: { "raw_document": { "text": text_to_analyze } }
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }

    res = requests.post(
        url=url,
        headers=headers,
        json=payload
    )

    try:
        res.raise_for_status()
        

        # return res.json()
        modified_res = res.json().get("emotionPredictions")[0].get("emotion")
        return modified_res

    except Exception as e:
        print(e)

        if res.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None
            }

        


if __name__ == "__main__":

    # text = "I love this new technology."
    # text = "I think I am having fun"

    text = None
    ic(emotion_detector(text))

