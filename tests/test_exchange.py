"""核对交换资料的字段和数值关系。"""
import json
from pathlib import Path
import unittest

import numpy as np


class ExchangeTests(unittest.TestCase):
    def setUp(self):
        source = Path(__file__).resolve().parents[1] / "data" / "exchange.json"
        self.data = json.loads(source.read_text(encoding="utf-8"))

    def test_exchange_data(self):
        events=self.data['events']
        self.assertEqual(events[0]['obs'],events[1]['obs'])
        self.assertNotEqual(events[0]['foot'],events[4]['foot'])
        self.assertTrue(set(events[4]['foot']) & set(self.data['masked']))
