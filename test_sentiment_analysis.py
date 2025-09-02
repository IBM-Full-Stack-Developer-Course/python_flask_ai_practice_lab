from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        case_1 = "I love working with Python"
        case_2 = "I hate working with Python"
        case_3 =  "I am neutral on Python"

        result = sentiment_analyzer(case_1)
        self.assertEqual(result['label'], 'SENT_POSITIVE')

        result_2 = sentiment_analyzer(case_2)
        self.assertEqual(result['label'], 'SENT_NEGATIVE')

        result_3 = sentiment_analyzer(case_3)
        self.assertEqual(result['label'], 'SENT_NEUTRAL')

unittest.main()