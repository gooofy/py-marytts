#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#
# Copyright 2017 Guenter Bartsch
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import unittest
import logging
from io import StringIO, BytesIO
import wave

from marytts import MaryTTS

G2P_TESTS = [
             (u"GELBSEIDENEN",     u"' g E l - ' b s AI - d i - n @ n"),
             (u"UNMUTE",           u"' @ n m - j u t"),
             (u"GESCHIRRSCHEUERN", u"' g E s r - S u r= n"),
             (u"DÜSTRE",           u"' d V s - t r="),
             (u"EINGANGE",         u"' AI N - g { n dZ"),
             (u"AUSSCHLÄGEN",      u"' O - s l EI - g @ n"),
             (u"NACHHÄNGEND",      u"' n { - k h { N - dZ E n d"),
             (u"HAUPTSTRAßEN",     u"' h O p t s - t r @ - s @ n"),
             (u"HOCHWEISEN",       u"' h A - ' tS w AI - s @ n"),
             (u"DICKER",           u"' d I - k r="),
            ]

class TestMaryTTS (unittest.TestCase):

    def test_voices(self):
        mtts = MaryTTS()

        voices = mtts.voices
        self.assertGreater (len(voices), 1)

    def test_synth_wav(self):

        mtts = MaryTTS(voice='cmu-rms-hsmm', locale='en_US')
        wavs = mtts.synth_wav('Hello World!')
        wav = wave.open(BytesIO(wavs))
        
        self.assertEqual   (wav.getnchannels(),     1)
        self.assertEqual   (wav.getframerate(), 16000)
        self.assertGreater (wav.getnframes(),   10000)

    def test_synth_wav_de(self):

        mtts = MaryTTS(voice='bits3', locale='de')
        wavs = mtts.synth_wav('Hallo Welt!')
        wav = wave.open(BytesIO(wavs))
        
        self.assertEqual   (wav.getnchannels(),     1)
        self.assertEqual   (wav.getframerate(), 16000)
        self.assertGreater (wav.getnframes(),   10000)

    def test_synth_wav_xsampa(self):

        mtts = MaryTTS()
        wavs = mtts.synth_wav("' AI N - g { n dZ", fmt='xs')
        wav = wave.open(BytesIO(wavs))
        
        self.assertEqual   (wav.getnchannels(),     1)
        self.assertEqual   (wav.getframerate(), 16000)
        self.assertGreater (wav.getnframes(),   10000)

    def test_g2p(self):
        mtts = MaryTTS()

        for g, xs_t in G2P_TESTS:

            xs  = mtts.g2p (g)
            self.assertEquals(xs, xs_t)

if __name__ == "__main__":

    # logging.basicConfig(level=logging.ERROR)
    logging.basicConfig(level=logging.DEBUG)

    unittest.main()

