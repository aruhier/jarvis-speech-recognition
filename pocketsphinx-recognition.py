#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys,os
import pocketsphinx as ps
import sphinxbase
import gst,gtk
import logging
import shutil
import time
import wave

# file where we record our voice (removed at end)
WAVFILE='/tmp/jarvis.wav'

# to be clean on logs
logging.getLogger().setLevel(logging.DEBUG)

hmmd = "/usr/share/pocketsphinx/model/hmm/fr_FR/lium_french_f0"
lmd = "/usr/share/pocketsphinx/model/lm/fr_FR/french3g62K.lm"
dictd = "/usr/share/pocketsphinx/model/lm/fr_FR/frenchWords62K.dic"

speechRec = ps.Decoder(hmm = hmmd, lm = lmd, dict = dictd)

def decodeSpeech():
    """
    Decodes a speech file
    """
    fh = open(WAVFILE, 'rb')
    fh.seek(44)
    speechRec.decode_raw(fh)
    result = speechRec.get_hyp()
    fh.close()

    return result[0]

def on_vader_start(ob, message):
    """ Just to be sure that vader has reconnized that you're speaking
    we set a trace """
    logging.debug("Listening...")

def on_vader_stop(ob, message):
    """ This function is launched when vader stopped to listen
    That happend when you stop to talk """

    logging.debug("Processing...")

    # pause pipeline to not break our file
    pipe.set_state(gst.STATE_PAUSED)

    try:
        result = decodeSpeech()
        print(result)
    except:
        logging.error("An error occured...")

    w = wave.open(WAVFILE, 'w')
    w.setparams((1, 1, 16000, 0, 'NONE', 'not compressed'))
    w.writeframes('h')
    w.close()
    pipe.set_state(gst.STATE_PLAYING)


#the main pipeline
pipe = gst.parse_launch('autoaudiosrc ! vader auto_threshold=true name=vad '
                        '! audioconvert ! audioresample ! '
                        'audio/x-raw-int,rate=16000 ! wavenc ! '
                        'filesink location=%s' % WAVFILE)
bus = pipe.get_bus()
bus.add_signal_watch()

vader = pipe.get_by_name('vad')
vader.connect('vader-start', on_vader_start)
vader.connect('vader-stop', on_vader_stop)

try:
    # start the pipeline now
    pipe.set_state(gst.STATE_PLAYING)
    logging.info("Press CTRL+C to stop")
    gtk.main()

except KeyboardInterrupt:
    # stop pipeline
    pipe.set_state(gst.STATE_NULL)
    # remove our flac file
    os.remove(WAVFILE)
