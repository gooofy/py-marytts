py-marytts
----------

A pretty simple HTTP based interface to MaryTTS intended to make using this excellent TTS
for waveform and IPA generation as convenient as possible. 

Target audience are developers who would like to use MaryTTS as-is for speech
synthesis in their Python application on GNU/Linux operating systems.

Constructive comments, patches and pull-requests are very welcome.

Examples
~~~~~~~~

First, imports:
[source,python]
----
import wave
import StringIO
from marytts import MaryTTS
----

english (default) synthesis:

[source,python]
----
marytts = MaryTTS()
wavs = marytts.synth_wav('Hello World!')
wav = wave.open(StringIO.StringIO(wavs))
print wav.getnchannels(), wav.getframerate(), wav.getnframes()
----
result:
----
1 16000 21520
----

try a different language:
[source,python]
----
marytts.locale = 'de'
marytts.voice  = 'bits3'
wavs = marytts.synth_wav('Hallo Welt!')
wav = wave.open(StringIO.StringIO(wavs))
print wav.getnchannels(), wav.getframerate(), wav.getnframes()
----
result:
----
1 16000 16760
----


List Available Voices
^^^^^^^^^^^^^^^^^^^^^
[source,python]
----
l = marytts.voices
----
result:
----
>>> l[0]
['upmc-pierre-hsmm', 'fr', 'male', 'hmm']
>>> l[1]
['dfki-pavoque-neutral-hsmm', 'de', 'male', 'hmm']
>>> l[2]
['cmu-slt-hsmm', 'en_US', 'female', 'hmm']
>>> l[3]
['cmu-rms-hsmm', 'en_US', 'male', 'hmm']
...
----

Grapheme to Phoneme (G2P) Conversion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[source,python]
----
marytts.locale = 'en_US'
marytts.voice  = 'cmu-rms-hsmm'
cs = marytts.g2p ('Hello World!')
----
result:
----
>>> cs
"h @ - ' l @U ' w r= l d"
----

Synthesize Phonemes
^^^^^^^^^^^^^^^^^^^
[source,python]
----
wavs = marytts.synth_wav("h @ - ' l @U ' w r= l d", fmt='xs')
wav = wave.open(StringIO.StringIO(wavs))
print wav.getnchannels(), wav.getframerate(), wav.getnframes()
----
result:
----
1 16000 21520
----

Links
~~~~~

* https://github.com/marytts/marytts [MaryTTS on github]

Requirements
~~~~~~~~~~~~

* Python 2.7
* MaryTTS server running

License
~~~~~~~

My own code is Apache-2.0 licensed unless otherwise noted in the script's copyright
headers.

Author
~~~~~~

Guenter Bartsch <guenter@zamia.org>

