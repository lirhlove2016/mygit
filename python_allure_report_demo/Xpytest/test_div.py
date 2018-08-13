#!/usr/bin/env python
#-*-coding:utf-8-*-

import  unittest

def div(a,b):
    return a-b


class DivTest(unittest.TestCase):
    def test_div_001(self):
        self.assertEqual(div(3,2),1)

    def test_div_002(self):
        self.assertEqual(div(3,3),0)

    def test_div_003(self):
        self.assertEqual(abs(div(2,3)),1)
