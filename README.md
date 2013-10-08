Jarvis-speech-recognition
=========================

Jarvis is a speech recognition assistant, which will use many API to get a maximum integration with every soft on your system.

For the moment Jarvis can just controll (in a minimalistic way) Banshee to play music, stop it and change the song,
and it's in french (but I will add a configuration file soon, to change easily the language).<br>
Also, the algorithm to match what the user says is bad for the moment, but I'm working on it.

For the speech recognition, it uses Google Speech or PocketSphinx, but I can not get good results with PocketSphinx for the moment,
so I advise you to use Google Speech.


Dependencies :
---------------

<ul>
  <li>PocketSphinx</li>
  <li>Python 2.7</li>
  <li>Gstreamer</li>
</ul>

<p>For ArchLinux :</p>
<ul>
  <li>sphinxbase (AUR)</li>
  <ll>pocketsphinx (AUR)</li>
  <li>python2</li>
  <li>gstreamer0.10-python</li>
</ul>

<p>For Ubuntu : </p>
<ul>
  <li>sphinxbase-utils</li>
  <li>python-sphinxbase>
  <li>pocketsphinx-utils</li>
  <li>gstreamer0.10-pocketsphinx</li>
  <li>python-minimal</li>
</ul>


How to :
--------

For the moment there are 3 ways to use Jarvis :
<ul>
  <li><b>Text mode :</b> launch "jarvis.py" and interact with Jarvis by typing,</li>
  <li><b>Speech Recognition using Google Speech :</b> launch "google-speech.py" and interact with Jarvis by voice,</li>
  <li><b>Speech Recognition using PocketSphinx :</b> launch "pocketsphinx-recognition.py" and (try to) interact with Jarvis
      (doesn't give good results for now).
</ul>
In the future, you will be able to set it in a configuration file.

When you write or speak to Jarvis, it will search in all the .txt in the "data" folder if something match. Then it will
launch the action set to this sentence (actions are in the "actions" folder).
