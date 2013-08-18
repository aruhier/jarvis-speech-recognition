#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys,os,time
import gst,gtk
import logging
import urllib2
import json
import match
import threading

# file where we record our voice (removed at end)
FLACFILE='/tmp/jarvis.flac'

# to be clean on logs
logging.getLogger().setLevel(logging.DEBUG)

def send2jarvis(request):
    if request.lower().find("jarvis") != -1 :
        match.search(request)

def googleSpeech(flacfile):
    req = urllib2.Request('https://www.google.com/speech-api/v1/'
                          'recognize?client=chromium&lang=fr-FR&maxresults=10',
                          flacfile.read(), {'Content-Type': 'audio/x-flac; rate=16000'})
    res = urllib2.urlopen(req)
    resp = res.read()
    resp = json.loads(resp)
    return str(resp['hypotheses'][0]['utterance'])


def on_vader_start(ob, message):
    """ Just to be sure that vader has reconnized that you're speaking
    we set a trace """
    logging.debug("Listening...")

def on_vader_stop(ob, message):
    """ This function is launched when vader stopped to listen
    That happend when you stop to talk """

    time.sleep(0.5)
    logging.debug("Processing...")

    # pause pipeline to not break our file
    pipe.set_state(gst.STATE_PAUSED)

    # get content of the file
    flacfile = file(FLACFILE, 'r')

    try:
        result = googleSpeech(flacfile)
        print result
        jarvis = threading.Thread(None, send2jarvis, None, (result, ))
        jarvis.start()
        jarvis.join()
    except:
        logging.error("An error occured...")

    file(FLACFILE, 'w').write('')

    #file is empty, continue to listen
    pipe.set_state(gst.STATE_PLAYING)


#the main pipeline
pipe = gst.parse_launch('autoaudiosrc ! vader auto_threshold=true name=vad '
                        '! audioconvert ! audioresample ! '
                        'audio/x-raw-int,rate=16000 ! flacenc ! '
                        'filesink location=%s' % FLACFILE)
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
    os.remove(FLACFILE)
