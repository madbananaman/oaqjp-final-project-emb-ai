import unittest

from icecream import ic

from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        # Test case for anger sentiment 
        result_anger = emotion_detector('I hate working long hours.') 
        max_result_anger = max(result_anger, key=result_anger.get)
        self.assertEqual(max_result_anger, "anger")

        # Statement	| Dominant Emotion
        #   - I am glad this happened	joy
        result_joy = emotion_detector('I am glad this happened') 
        max_result_joy = max(result_joy, key=result_joy.get)
        self.assertEqual(max_result_joy, "joy")

        #   - I am really mad about this	anger
        result_3 = emotion_detector('I am really mad about this') 
        max_result_3 = max(result_3, key=result_3.get)
        self.assertEqual(max_result_3, "anger")

        #   - I feel disgusted just hearing about this	disgust
        result_4 = emotion_detector('I feel disgusted just hearing about this') 
        max_result_4 = max(result_4, key=result_4.get)
        self.assertEqual(max_result_4, "disgust")

        #   - I am so sad about this	sadness
        result_5 = emotion_detector('I am so sad about this') 
        max_result_5 = max(result_5, key=result_5.get)
        self.assertEqual(max_result_5, "sadness")

        #   - I am really afraid that this will happen	fear
        result_6 = emotion_detector('I am really afraid that this will happen') 
        max_result_6 = max(result_6, key=result_6.get)
        self.assertEqual(max_result_6, "fear")






if __name__ == "__main__":
    unittest.main()
