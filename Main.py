#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on November 29, 2019, at 20:43
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'Main'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='G:\\PsychoPy\\AMP\\Main.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "practiceInstruction"
practiceInstructionClock = core.Clock()
practiceInstructionText = visual.TextStim(win=win, name='practiceInstructionText',
    text='بر روی صفحه\u200cی مانیتور پیش از هر حرف الفبای چینی\nیک تصویر مربوط به یک چشم\u200cانداز روزانه ظاهر می\u200cشود\nو خیلی مهم است که بدون متأثر شدن از از این تصاویر بر ارزیابی حرف چینی تمرکز کنید.\n\nاگر حرف چینی به نظرتان خوشایند آمد، بعد از نمایش صفحه\u200cی سیاه و سفید\nکلید I و اگر ناخوشایند بود کلید E را فشار دهید.\n\nدرصورت آمادگی برای تمرین آزمون و آشنایی با آن،\nکلید فاصله را فشار دهید.',
    font='Calibri',
    pos=(0, 0), height=0.030, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=0.0);
practiceInstructionKeyboard = keyboard.Keyboard()

# Initialize components for Routine "practice"
practiceClock = core.Clock()
practiceKey = ''
practicePrimeImage = visual.ImageStim(
    win=win,
    name='practicePrimeImage', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
practiceBlankSection = visual.Rect(
    win=win, name='practiceBlankSection',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
practiceTargetImage = visual.ImageStim(
    win=win,
    name='practiceTargetImage', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
practiceResponseSection = visual.NoiseStim(
    win=win, name='practiceResponseSection',
    noiseImage=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5), sf=None,
    phase=0.0,
    color=[1,1,1], colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=128, filter=None,
    noiseType='Uniform', noiseElementSize=0.0625, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-4.0)
practiceResponseSection.buildNoise()
practiceResponseKeyboard = keyboard.Keyboard()

# Initialize components for Routine "practiceFeedback"
practiceFeedbackClock = core.Clock()
feedbackText = visual.TextStim(win=win, name='feedbackText',
    text='default text',
    font='Calibri',
    pos=(0, 0), height=0.060, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=-1.0);
feedbackISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='feedbackISI')

# Initialize components for Routine "trialInstruction"
trialInstructionClock = core.Clock()
trialInstructionText = visual.TextStim(win=win, name='trialInstructionText',
    text='حال که مکان کلید خوشایندی و ناخوشایندی را یاد گرفتید،\nوارد آزمون اصلی می\u200cشویم که از تعداد تصاویر بیشتری تشکیل شده\nو پاسخ\u200cهای شما در آن ثبت می\u200cشود.\n\nلطفاً برای شروع کلید فاصله را فشار دهید.\n',
    font='Calibri',
    pos=(0, 0), height=0.030, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=0.0);
trialInstructionKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
primeImage = visual.ImageStim(
    win=win,
    name='primeImage', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
blankSection = visual.Rect(
    win=win, name='blankSection',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor='white', fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
targetImage = visual.ImageStim(
    win=win,
    name='targetImage', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
responseSection = visual.NoiseStim(
    win=win, name='responseSection',
    noiseImage=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5), sf=None,
    phase=0.0,
    color=[1,1,1], colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=128, filter=None,
    noiseType='Uniform', noiseElementSize=0.0625, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-3.0)
responseSection.buildNoise()
responseKeyboard = keyboard.Keyboard()

# Initialize components for Routine "finish"
finishClock = core.Clock()
finishText = visual.TextStim(win=win, name='finishText',
    text='از همکاری شما سپاسگذاریم.',
    font='Calibri',
    pos=(0, 0), height=0.050, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=0.0);
finishKeyboard = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "practiceInstruction"-------
# update component parameters for each repeat
practiceInstructionKeyboard.keys = []
practiceInstructionKeyboard.rt = []
# keep track of which components have finished
practiceInstructionComponents = [practiceInstructionText, practiceInstructionKeyboard]
for thisComponent in practiceInstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practiceInstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "practiceInstruction"-------
while continueRoutine:
    # get current time
    t = practiceInstructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practiceInstructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practiceInstructionText* updates
    if practiceInstructionText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceInstructionText.frameNStart = frameN  # exact frame index
        practiceInstructionText.tStart = t  # local t and not account for scr refresh
        practiceInstructionText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceInstructionText, 'tStartRefresh')  # time at next scr refresh
        practiceInstructionText.setAutoDraw(True)
    
    # *practiceInstructionKeyboard* updates
    waitOnFlip = False
    if practiceInstructionKeyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practiceInstructionKeyboard.frameNStart = frameN  # exact frame index
        practiceInstructionKeyboard.tStart = t  # local t and not account for scr refresh
        practiceInstructionKeyboard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practiceInstructionKeyboard, 'tStartRefresh')  # time at next scr refresh
        practiceInstructionKeyboard.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(practiceInstructionKeyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if practiceInstructionKeyboard.status == STARTED and not waitOnFlip:
        theseKeys = practiceInstructionKeyboard.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practiceInstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practiceInstruction"-------
for thisComponent in practiceInstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practiceInstructionText.started', practiceInstructionText.tStartRefresh)
thisExp.addData('practiceInstructionText.stopped', practiceInstructionText.tStopRefresh)
# the Routine "practiceInstruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practices = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images.xlsx', selection='20:30'),
    seed=None, name='practices')
thisExp.addLoop(practices)  # add the loop to the experiment
thisPractice = practices.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
if thisPractice != None:
    for paramName in thisPractice:
        exec('{} = thisPractice[paramName]'.format(paramName))

for thisPractice in practices:
    currentLoop = practices
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            exec('{} = thisPractice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practice"-------
    # update component parameters for each repeat
    practiceKey = ''
    practicePrimeImage.setImage(primeStim)
    practiceTargetImage.setImage(targetStim)
    practiceResponseKeyboard.keys = []
    practiceResponseKeyboard.rt = []
    # keep track of which components have finished
    practiceComponents = [practicePrimeImage, practiceBlankSection, practiceTargetImage, practiceResponseSection, practiceResponseKeyboard]
    for thisComponent in practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "practice"-------
    while continueRoutine:
        # get current time
        t = practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practicePrimeImage* updates
        if practicePrimeImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practicePrimeImage.frameNStart = frameN  # exact frame index
            practicePrimeImage.tStart = t  # local t and not account for scr refresh
            practicePrimeImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practicePrimeImage, 'tStartRefresh')  # time at next scr refresh
            practicePrimeImage.setAutoDraw(True)
        if practicePrimeImage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > practicePrimeImage.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                practicePrimeImage.tStop = t  # not accounting for scr refresh
                practicePrimeImage.frameNStop = frameN  # exact frame index
                win.timeOnFlip(practicePrimeImage, 'tStopRefresh')  # time at next scr refresh
                practicePrimeImage.setAutoDraw(False)
        
        # *practiceBlankSection* updates
        if practiceBlankSection.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
            # keep track of start time/frame for later
            practiceBlankSection.frameNStart = frameN  # exact frame index
            practiceBlankSection.tStart = t  # local t and not account for scr refresh
            practiceBlankSection.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practiceBlankSection, 'tStartRefresh')  # time at next scr refresh
            practiceBlankSection.setAutoDraw(True)
        if practiceBlankSection.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > practiceBlankSection.tStartRefresh + 0.125-frameTolerance:
                # keep track of stop time/frame for later
                practiceBlankSection.tStop = t  # not accounting for scr refresh
                practiceBlankSection.frameNStop = frameN  # exact frame index
                win.timeOnFlip(practiceBlankSection, 'tStopRefresh')  # time at next scr refresh
                practiceBlankSection.setAutoDraw(False)
        
        # *practiceTargetImage* updates
        if practiceTargetImage.status == NOT_STARTED and tThisFlip >= 0.225-frameTolerance:
            # keep track of start time/frame for later
            practiceTargetImage.frameNStart = frameN  # exact frame index
            practiceTargetImage.tStart = t  # local t and not account for scr refresh
            practiceTargetImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practiceTargetImage, 'tStartRefresh')  # time at next scr refresh
            practiceTargetImage.setAutoDraw(True)
        if practiceTargetImage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > practiceTargetImage.tStartRefresh + 0.125-frameTolerance:
                # keep track of stop time/frame for later
                practiceTargetImage.tStop = t  # not accounting for scr refresh
                practiceTargetImage.frameNStop = frameN  # exact frame index
                win.timeOnFlip(practiceTargetImage, 'tStopRefresh')  # time at next scr refresh
                practiceTargetImage.setAutoDraw(False)
        
        # *practiceResponseSection* updates
        if practiceResponseSection.status == NOT_STARTED and tThisFlip >= 0.350-frameTolerance:
            # keep track of start time/frame for later
            practiceResponseSection.frameNStart = frameN  # exact frame index
            practiceResponseSection.tStart = t  # local t and not account for scr refresh
            practiceResponseSection.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practiceResponseSection, 'tStartRefresh')  # time at next scr refresh
            practiceResponseSection.setAutoDraw(True)
        if practiceResponseSection.status == STARTED:
            if practiceResponseSection._needBuild:
                practiceResponseSection.buildNoise()
        
        # *practiceResponseKeyboard* updates
        waitOnFlip = False
        if practiceResponseKeyboard.status == NOT_STARTED and tThisFlip >= 0.350-frameTolerance:
            # keep track of start time/frame for later
            practiceResponseKeyboard.frameNStart = frameN  # exact frame index
            practiceResponseKeyboard.tStart = t  # local t and not account for scr refresh
            practiceResponseKeyboard.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practiceResponseKeyboard, 'tStartRefresh')  # time at next scr refresh
            practiceResponseKeyboard.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(practiceResponseKeyboard.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(practiceResponseKeyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if practiceResponseKeyboard.status == STARTED and not waitOnFlip:
            theseKeys = practiceResponseKeyboard.getKeys(keyList=['e', 'i'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if practiceResponseKeyboard.keys == []:  # then this was the first keypress
                    practiceResponseKeyboard.keys = theseKeys.name  # just the first key pressed
                    practiceResponseKeyboard.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice"-------
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceKey = practiceResponseKeyboard.keys
    practices.addData('practicePrimeImage.started', practicePrimeImage.tStartRefresh)
    practices.addData('practicePrimeImage.stopped', practicePrimeImage.tStopRefresh)
    practices.addData('practiceBlankSection.started', practiceBlankSection.tStartRefresh)
    practices.addData('practiceBlankSection.stopped', practiceBlankSection.tStopRefresh)
    practices.addData('practiceTargetImage.started', practiceTargetImage.tStartRefresh)
    practices.addData('practiceTargetImage.stopped', practiceTargetImage.tStopRefresh)
    practices.addData('practiceResponseSection.started', practiceResponseSection.tStartRefresh)
    practices.addData('practiceResponseSection.stopped', practiceResponseSection.tStopRefresh)
    # check responses
    if practiceResponseKeyboard.keys in ['', [], None]:  # No response was made
        practiceResponseKeyboard.keys = None
    practices.addData('practiceResponseKeyboard.keys',practiceResponseKeyboard.keys)
    if practiceResponseKeyboard.keys != None:  # we had a response
        practices.addData('practiceResponseKeyboard.rt', practiceResponseKeyboard.rt)
    practices.addData('practiceResponseKeyboard.started', practiceResponseKeyboard.tStartRefresh)
    practices.addData('practiceResponseKeyboard.stopped', practiceResponseKeyboard.tStopRefresh)
    # the Routine "practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "practiceFeedback"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    if practiceKey == 'e' :
        feedbackEntryText = "خوشایند"
    else :
        feedbackEntryText = "ناخوشایند"
    # keep track of which components have finished
    practiceFeedbackComponents = [feedbackText, feedbackISI]
    for thisComponent in practiceFeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practiceFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "practiceFeedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practiceFeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceFeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedbackText* updates
        if feedbackText.status == NOT_STARTED and tThisFlip >= 0.05-frameTolerance:
            # keep track of start time/frame for later
            feedbackText.frameNStart = frameN  # exact frame index
            feedbackText.tStart = t  # local t and not account for scr refresh
            feedbackText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbackText, 'tStartRefresh')  # time at next scr refresh
            feedbackText.setAutoDraw(True)
        if feedbackText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbackText.tStartRefresh + 0.45-frameTolerance:
                # keep track of stop time/frame for later
                feedbackText.tStop = t  # not accounting for scr refresh
                feedbackText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedbackText, 'tStopRefresh')  # time at next scr refresh
                feedbackText.setAutoDraw(False)
        # *feedbackISI* period
        if feedbackISI.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedbackISI.frameNStart = frameN  # exact frame index
            feedbackISI.tStart = t  # local t and not account for scr refresh
            feedbackISI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbackISI, 'tStartRefresh')  # time at next scr refresh
            feedbackISI.start(0.05)
        elif feedbackISI.status == STARTED:  # one frame should pass before updating params and completing
            # updating other components during *feedbackISI*
            feedbackText.setText(feedbackEntryText)
            # component updates done
            feedbackISI.complete()  # finish the static period
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceFeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practiceFeedback"-------
    for thisComponent in practiceFeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practices.addData('feedbackText.started', feedbackText.tStartRefresh)
    practices.addData('feedbackText.stopped', feedbackText.tStopRefresh)
    practices.addData('feedbackISI.started', feedbackISI.tStart)
    practices.addData('feedbackISI.stopped', feedbackISI.tStop)
# completed 1 repeats of 'practices'


# ------Prepare to start Routine "trialInstruction"-------
# update component parameters for each repeat
trialInstructionKeyboard.keys = []
trialInstructionKeyboard.rt = []
# keep track of which components have finished
trialInstructionComponents = [trialInstructionText, trialInstructionKeyboard]
for thisComponent in trialInstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialInstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trialInstruction"-------
while continueRoutine:
    # get current time
    t = trialInstructionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialInstructionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *trialInstructionText* updates
    if trialInstructionText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trialInstructionText.frameNStart = frameN  # exact frame index
        trialInstructionText.tStart = t  # local t and not account for scr refresh
        trialInstructionText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trialInstructionText, 'tStartRefresh')  # time at next scr refresh
        trialInstructionText.setAutoDraw(True)
    
    # *trialInstructionKeyboard* updates
    waitOnFlip = False
    if trialInstructionKeyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trialInstructionKeyboard.frameNStart = frameN  # exact frame index
        trialInstructionKeyboard.tStart = t  # local t and not account for scr refresh
        trialInstructionKeyboard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trialInstructionKeyboard, 'tStartRefresh')  # time at next scr refresh
        trialInstructionKeyboard.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(trialInstructionKeyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if trialInstructionKeyboard.status == STARTED and not waitOnFlip:
        theseKeys = trialInstructionKeyboard.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialInstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trialInstruction"-------
for thisComponent in trialInstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('trialInstructionText.started', trialInstructionText.tStartRefresh)
thisExp.addData('trialInstructionText.stopped', trialInstructionText.tStopRefresh)
# the Routine "trialInstruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    # update component parameters for each repeat
    primeImage.setImage(primeStim)
    targetImage.setImage(targetStim)
    responseKeyboard.keys = []
    responseKeyboard.rt = []
    # keep track of which components have finished
    trialComponents = [primeImage, blankSection, targetImage, responseSection, responseKeyboard]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *primeImage* updates
        if primeImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            primeImage.frameNStart = frameN  # exact frame index
            primeImage.tStart = t  # local t and not account for scr refresh
            primeImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(primeImage, 'tStartRefresh')  # time at next scr refresh
            primeImage.setAutoDraw(True)
        if primeImage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > primeImage.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                primeImage.tStop = t  # not accounting for scr refresh
                primeImage.frameNStop = frameN  # exact frame index
                win.timeOnFlip(primeImage, 'tStopRefresh')  # time at next scr refresh
                primeImage.setAutoDraw(False)
        
        # *blankSection* updates
        if blankSection.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
            # keep track of start time/frame for later
            blankSection.frameNStart = frameN  # exact frame index
            blankSection.tStart = t  # local t and not account for scr refresh
            blankSection.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blankSection, 'tStartRefresh')  # time at next scr refresh
            blankSection.setAutoDraw(True)
        if blankSection.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blankSection.tStartRefresh + 0.125-frameTolerance:
                # keep track of stop time/frame for later
                blankSection.tStop = t  # not accounting for scr refresh
                blankSection.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blankSection, 'tStopRefresh')  # time at next scr refresh
                blankSection.setAutoDraw(False)
        
        # *targetImage* updates
        if targetImage.status == NOT_STARTED and tThisFlip >= 0.225-frameTolerance:
            # keep track of start time/frame for later
            targetImage.frameNStart = frameN  # exact frame index
            targetImage.tStart = t  # local t and not account for scr refresh
            targetImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(targetImage, 'tStartRefresh')  # time at next scr refresh
            targetImage.setAutoDraw(True)
        if targetImage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > targetImage.tStartRefresh + 0.125-frameTolerance:
                # keep track of stop time/frame for later
                targetImage.tStop = t  # not accounting for scr refresh
                targetImage.frameNStop = frameN  # exact frame index
                win.timeOnFlip(targetImage, 'tStopRefresh')  # time at next scr refresh
                targetImage.setAutoDraw(False)
        
        # *responseSection* updates
        if responseSection.status == NOT_STARTED and tThisFlip >= 0.350-frameTolerance:
            # keep track of start time/frame for later
            responseSection.frameNStart = frameN  # exact frame index
            responseSection.tStart = t  # local t and not account for scr refresh
            responseSection.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(responseSection, 'tStartRefresh')  # time at next scr refresh
            responseSection.setAutoDraw(True)
        if responseSection.status == STARTED:
            if responseSection._needBuild:
                responseSection.buildNoise()
        
        # *responseKeyboard* updates
        waitOnFlip = False
        if responseKeyboard.status == NOT_STARTED and tThisFlip >= 0.350-frameTolerance:
            # keep track of start time/frame for later
            responseKeyboard.frameNStart = frameN  # exact frame index
            responseKeyboard.tStart = t  # local t and not account for scr refresh
            responseKeyboard.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(responseKeyboard, 'tStartRefresh')  # time at next scr refresh
            responseKeyboard.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(responseKeyboard.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(responseKeyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if responseKeyboard.status == STARTED and not waitOnFlip:
            theseKeys = responseKeyboard.getKeys(keyList=['e', 'i'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if responseKeyboard.keys == []:  # then this was the first keypress
                    responseKeyboard.keys = theseKeys.name  # just the first key pressed
                    responseKeyboard.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('primeImage.started', primeImage.tStartRefresh)
    trials.addData('primeImage.stopped', primeImage.tStopRefresh)
    trials.addData('blankSection.started', blankSection.tStartRefresh)
    trials.addData('blankSection.stopped', blankSection.tStopRefresh)
    trials.addData('targetImage.started', targetImage.tStartRefresh)
    trials.addData('targetImage.stopped', targetImage.tStopRefresh)
    trials.addData('responseSection.started', responseSection.tStartRefresh)
    trials.addData('responseSection.stopped', responseSection.tStopRefresh)
    # check responses
    if responseKeyboard.keys in ['', [], None]:  # No response was made
        responseKeyboard.keys = None
    trials.addData('responseKeyboard.keys',responseKeyboard.keys)
    if responseKeyboard.keys != None:  # we had a response
        trials.addData('responseKeyboard.rt', responseKeyboard.rt)
    trials.addData('responseKeyboard.started', responseKeyboard.tStartRefresh)
    trials.addData('responseKeyboard.stopped', responseKeyboard.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "finish"-------
# update component parameters for each repeat
finishKeyboard.keys = []
finishKeyboard.rt = []
# keep track of which components have finished
finishComponents = [finishText, finishKeyboard]
for thisComponent in finishComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
finishClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "finish"-------
while continueRoutine:
    # get current time
    t = finishClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=finishClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *finishText* updates
    if finishText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finishText.frameNStart = frameN  # exact frame index
        finishText.tStart = t  # local t and not account for scr refresh
        finishText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finishText, 'tStartRefresh')  # time at next scr refresh
        finishText.setAutoDraw(True)
    
    # *finishKeyboard* updates
    waitOnFlip = False
    if finishKeyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finishKeyboard.frameNStart = frameN  # exact frame index
        finishKeyboard.tStart = t  # local t and not account for scr refresh
        finishKeyboard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finishKeyboard, 'tStartRefresh')  # time at next scr refresh
        finishKeyboard.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(finishKeyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if finishKeyboard.status == STARTED and not waitOnFlip:
        theseKeys = finishKeyboard.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finishComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "finish"-------
for thisComponent in finishComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('finishText.started', finishText.tStartRefresh)
thisExp.addData('finishText.stopped', finishText.tStopRefresh)
# the Routine "finish" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
