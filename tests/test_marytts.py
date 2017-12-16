#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#
# Copyright 2017 Guenter Bartsch
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
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

