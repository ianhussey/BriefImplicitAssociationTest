#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Mon Oct 19 17:10:19 2015
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'BIAT'  # from the Builder filename that created this script
expInfo = {u'gender': u'', u'age': u'', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1280, 1024), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=u'black', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instructions1"
instructions1Clock = core.Clock()
category1Label = visual.TextStim(win=win, ori=0, name='category1Label',
    text='FLOWERS',    font='Arial',
    pos=[0, 0.9], height=0.1, wrapWidth=None,
    color=[-1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    depth=-1.0)
category1Stimuli = visual.TextStim(win=win, ori=0, name='category1Stimuli',
    text='Orchid Lily Violet Daisy',    font='Arial',
    pos=[0, 0.8], height=0.06, wrapWidth=None,
    color=[-1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    depth=-2.0)
attributeLabel = visual.TextStim(win=win, ori=0, name='attributeLabel',
    text='GOOD',    font='Arial',
    pos=[0, 0.5], height=0.1, wrapWidth=None,
    color=[1.000,1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-3.0)
attributeStimuli = visual.TextStim(win=win, ori=0, name='attributeStimuli',
    text='Wonderful Best Superb Excellent',    font='Arial',
    pos=[0, 0.4], height=0.06, wrapWidth=None,
    color=[1.000,1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-4.0)
orLabel = visual.TextStim(win=win, ori=0, name='orLabel',
    text='or',    font='Arial',
    pos=[0, 0.65], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
pressI1 = visual.TextStim(win=win, ori=0, name='pressI1',
    text='Press the I key for GOOD or FLOWERS',    font='Arial',
    pos=[0, 0], height=0.06, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0)
pressE = visual.TextStim(win=win, ori=0, name='pressE',
    text='Press the E key for anything else',    font='Arial',
    pos=[0, -.1], height=0.06, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0)
goFast = visual.TextStim(win=win, ori=0, name='goFast',
    text='Go as fast as you can',    font='Arial',
    pos=[0, -.3], height=0.06, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0)
pressSpace = visual.TextStim(win=win, ori=0, name='pressSpace',
    text='Press the space bar to begin',    font='Arial',
    pos=[0, -.5], height=0.06, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0)


# Initialize components for Routine "trial1FourTrials"
trial1FourTrialsClock = core.Clock()
stimulus1_2 = visual.TextStim(win=win, ori=0, name='stimulus1_2',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0)
msg1=""
accuracyFeedback1_2 = visual.TextStim(win=win, ori=0, name='accuracyFeedback1_2',
    text='default text',    font='Arial',
    pos=[0, -.5], height=0.15, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-4.0)
target1_2 = visual.TextStim(win=win, ori=0, name='target1_2',
    text='default text',    font='Arial',
    pos=[0, .8], height=0.06, wrapWidth=None,
    color=[-1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    depth=-5.0)
attribute1_2 = visual.TextStim(win=win, ori=0, name='attribute1_2',
    text='default text',    font='Arial',
    pos=[0, 0.6], height=0.06, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-6.0)
or1_2 = visual.TextStim(win=win, ori=0, name='or1_2',
    text='or',    font='Arial',
    pos=[0, 0.7], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0)


# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
stimulus1 = visual.TextStim(win=win, ori=0, name='stimulus1',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0)
msg1=""
accuracyFeedback1 = visual.TextStim(win=win, ori=0, name='accuracyFeedback1',
    text='default text',    font='Arial',
    pos=[0, -.5], height=0.15, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-4.0)
target1 = visual.TextStim(win=win, ori=0, name='target1',
    text='default text',    font='Arial',
    pos=[0, .8], height=0.06, wrapWidth=None,
    color=[-1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    depth=-5.0)
attribute1 = visual.TextStim(win=win, ori=0, name='attribute1',
    text='default text',    font='Arial',
    pos=[0, 0.6], height=0.06, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-6.0)
or1 = visual.TextStim(win=win, ori=0, name='or1',
    text='or',    font='Arial',
    pos=[0, 0.7], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0)

# Initialize components for Routine "instructions2"
instructions2Clock = core.Clock()
category2Label = visual.TextStim(win=win, ori=0, name='category2Label',
    text='INSECTS',    font='Arial',
    pos=[0, 0.9], height=0.1, wrapWidth=None,
    color=[-1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    depth=-1.0)
category2Stimuli = visual.TextStim(win=win, ori=0, name='category2Stimuli',
    text='Ant Locust Bee Wasp',    font='Arial',
    pos=[0, 0.8], height=0.06, wrapWidth=None,
    color=[-1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    depth=-2.0)
attributeLabel2 = visual.TextStim(win=win, ori=0, name='attributeLabel2',
    text='GOOD',    font='Arial',
    pos=[0, 0.5], height=0.1, wrapWidth=None,
    color=[1.000,1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-3.0)
attributeStimuli2 = visual.TextStim(win=win, ori=0, name='attributeStimuli2',
    text='Wonderful Best Superb Excellent',    font='Arial',
    pos=[0, 0.4], height=0.06, wrapWidth=None,
    color=[1.000,1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-4.0)
orLabel2 = visual.TextStim(win=win, ori=0, name='orLabel2',
    text='or',    font='Arial',
    pos=[0, 0.65], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
pressI2 = visual.TextStim(win=win, ori=0, name='pressI2',
    text='Press the I key for GOOD or INSECTS',    font='Arial',
    pos=[0, 0], height=0.06, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0)
pressE2 = visual.TextStim(win=win, ori=0, name='pressE2',
    text='Press the E key for anything else',    font='Arial',
    pos=[0, -.1], height=0.06, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0)
goFast2 = visual.TextStim(win=win, ori=0, name='goFast2',
    text='Go as fast as you can',    font='Arial',
    pos=[0, -.3], height=0.06, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0)
pressSpace2 = visual.TextStim(win=win, ori=0, name='pressSpace2',
    text='Press the space bar to begin',    font='Arial',
    pos=[0, -.5], height=0.06, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0)


# Initialize components for Routine "trial2FourTrials"
trial2FourTrialsClock = core.Clock()
stimulus2_2 = visual.TextStim(win=win, ori=0, name='stimulus2_2',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0)
msg2=""
accuracyFeedback2_2 = visual.TextStim(win=win, ori=0, name='accuracyFeedback2_2',
    text='default text',    font='Arial',
    pos=[0, -.5], height=0.15, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-4.0)
target2_2 = visual.TextStim(win=win, ori=0, name='target2_2',
    text='default text',    font='Arial',
    pos=[0, .8], height=0.06, wrapWidth=None,
    color=[-1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    depth=-5.0)
attribute2_2 = visual.TextStim(win=win, ori=0, name='attribute2_2',
    text='default text',    font='Arial',
    pos=[0, 0.6], height=0.06, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-6.0)
or2_2 = visual.TextStim(win=win, ori=0, name='or2_2',
    text='or',    font='Arial',
    pos=[0, 0.7], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0)


# Initialize components for Routine "trial2"
trial2Clock = core.Clock()
stimulus2 = visual.TextStim(win=win, ori=0, name='stimulus2',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0)
msg2=""
accuracyFeedback2 = visual.TextStim(win=win, ori=0, name='accuracyFeedback2',
    text='default text',    font='Arial',
    pos=[0, -.5], height=0.15, wrapWidth=None,
    color='red', colorSpace='rgb', opacity=1,
    depth=-4.0)
target2 = visual.TextStim(win=win, ori=0, name='target2',
    text='default text',    font='Arial',
    pos=[0, .8], height=0.06, wrapWidth=None,
    color=[-1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    depth=-5.0)
attribute2 = visual.TextStim(win=win, ori=0, name='attribute2',
    text='default text',    font='Arial',
    pos=[0, 0.6], height=0.06, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-6.0)
or2 = visual.TextStim(win=win, ori=0, name='or2',
    text='or',    font='Arial',
    pos=[0, 0.7], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0)

# Initialize components for Routine "end"
endClock = core.Clock()
endMessage = visual.TextStim(win=win, ori=0, name='endMessage',
    text='Please contact the researcher',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
repeatBlockPairLoop = data.TrialHandler(nReps=2, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=[None],
    seed=None, name='repeatBlockPairLoop')
thisExp.addLoop(repeatBlockPairLoop)  # add the loop to the experiment
thisRepeatBlockPairLoop = repeatBlockPairLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisRepeatBlockPairLoop.rgb)
if thisRepeatBlockPairLoop != None:
    for paramName in thisRepeatBlockPairLoop.keys():
        exec(paramName + '= thisRepeatBlockPairLoop.' + paramName)

for thisRepeatBlockPairLoop in repeatBlockPairLoop:
    currentLoop = repeatBlockPairLoop
    # abbreviate parameter names if possible (e.g. rgb = thisRepeatBlockPairLoop.rgb)
    if thisRepeatBlockPairLoop != None:
        for paramName in thisRepeatBlockPairLoop.keys():
            exec(paramName + '= thisRepeatBlockPairLoop.' + paramName)
    
    #------Prepare to start Routine "instructions1"-------
    t = 0
    instructions1Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    contResponse1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    contResponse1.status = NOT_STARTED
    trialsCounter = 0
    # keep track of which components have finished
    instructions1Components = []
    instructions1Components.append(contResponse1)
    instructions1Components.append(category1Label)
    instructions1Components.append(category1Stimuli)
    instructions1Components.append(attributeLabel)
    instructions1Components.append(attributeStimuli)
    instructions1Components.append(orLabel)
    instructions1Components.append(pressI1)
    instructions1Components.append(pressE)
    instructions1Components.append(goFast)
    instructions1Components.append(pressSpace)
    for thisComponent in instructions1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions1"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructions1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *contResponse1* updates
        if t >= 0.0 and contResponse1.status == NOT_STARTED:
            # keep track of start time/frame for later
            contResponse1.tStart = t  # underestimates by a little under one frame
            contResponse1.frameNStart = frameN  # exact frame index
            contResponse1.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if contResponse1.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # *category1Label* updates
        if t >= 0.0 and category1Label.status == NOT_STARTED:
            # keep track of start time/frame for later
            category1Label.tStart = t  # underestimates by a little under one frame
            category1Label.frameNStart = frameN  # exact frame index
            category1Label.setAutoDraw(True)
        
        # *category1Stimuli* updates
        if t >= 0.0 and category1Stimuli.status == NOT_STARTED:
            # keep track of start time/frame for later
            category1Stimuli.tStart = t  # underestimates by a little under one frame
            category1Stimuli.frameNStart = frameN  # exact frame index
            category1Stimuli.setAutoDraw(True)
        
        # *attributeLabel* updates
        if t >= 0.0 and attributeLabel.status == NOT_STARTED:
            # keep track of start time/frame for later
            attributeLabel.tStart = t  # underestimates by a little under one frame
            attributeLabel.frameNStart = frameN  # exact frame index
            attributeLabel.setAutoDraw(True)
        
        # *attributeStimuli* updates
        if t >= 0.0 and attributeStimuli.status == NOT_STARTED:
            # keep track of start time/frame for later
            attributeStimuli.tStart = t  # underestimates by a little under one frame
            attributeStimuli.frameNStart = frameN  # exact frame index
            attributeStimuli.setAutoDraw(True)
        
        # *orLabel* updates
        if t >= 0.0 and orLabel.status == NOT_STARTED:
            # keep track of start time/frame for later
            orLabel.tStart = t  # underestimates by a little under one frame
            orLabel.frameNStart = frameN  # exact frame index
            orLabel.setAutoDraw(True)
        
        # *pressI1* updates
        if t >= 0.0 and pressI1.status == NOT_STARTED:
            # keep track of start time/frame for later
            pressI1.tStart = t  # underestimates by a little under one frame
            pressI1.frameNStart = frameN  # exact frame index
            pressI1.setAutoDraw(True)
        
        # *pressE* updates
        if t >= 0.0 and pressE.status == NOT_STARTED:
            # keep track of start time/frame for later
            pressE.tStart = t  # underestimates by a little under one frame
            pressE.frameNStart = frameN  # exact frame index
            pressE.setAutoDraw(True)
        
        # *goFast* updates
        if t >= 0.0 and goFast.status == NOT_STARTED:
            # keep track of start time/frame for later
            goFast.tStart = t  # underestimates by a little under one frame
            goFast.frameNStart = frameN  # exact frame index
            goFast.setAutoDraw(True)
        
        # *pressSpace* updates
        if t >= 0.0 and pressSpace.status == NOT_STARTED:
            # keep track of start time/frame for later
            pressSpace.tStart = t  # underestimates by a little under one frame
            pressSpace.frameNStart = frameN  # exact frame index
            pressSpace.setAutoDraw(True)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions1"-------
    for thisComponent in instructions1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "instructions1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trial1Loop1FourTrials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions('categoryStimuli.xlsx'),
        seed=None, name='trial1Loop1FourTrials')
    thisExp.addLoop(trial1Loop1FourTrials)  # add the loop to the experiment
    thisTrial1Loop1FourTrial = trial1Loop1FourTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrial1Loop1FourTrial.rgb)
    if thisTrial1Loop1FourTrial != None:
        for paramName in thisTrial1Loop1FourTrial.keys():
            exec(paramName + '= thisTrial1Loop1FourTrial.' + paramName)
    
    for thisTrial1Loop1FourTrial in trial1Loop1FourTrials:
        currentLoop = trial1Loop1FourTrials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial1Loop1FourTrial.rgb)
        if thisTrial1Loop1FourTrial != None:
            for paramName in thisTrial1Loop1FourTrial.keys():
                exec(paramName + '= thisTrial1Loop1FourTrial.' + paramName)
        
        #------Prepare to start Routine "trial1FourTrials"-------
        t = 0
        trial1FourTrialsClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        stimulus1_2.setColor(stimulusColour, colorSpace='rgb')
        stimulus1_2.setText(stimulusVariable1)
        responseCorr1_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        responseCorr1_2.status = NOT_STARTED
        responseIncor1_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        responseIncor1_2.status = NOT_STARTED
        
        target1_2.setText(target1Text)
        attribute1_2.setColor([1.000,1.000,-1.000], colorSpace='rgb')
        attribute1_2.setText(attributeText)
        trialsCounter = trialsCounter + 1
        
        # keep track of which components have finished
        trial1FourTrialsComponents = []
        trial1FourTrialsComponents.append(stimulus1_2)
        trial1FourTrialsComponents.append(responseCorr1_2)
        trial1FourTrialsComponents.append(responseIncor1_2)
        trial1FourTrialsComponents.append(accuracyFeedback1_2)
        trial1FourTrialsComponents.append(target1_2)
        trial1FourTrialsComponents.append(attribute1_2)
        trial1FourTrialsComponents.append(or1_2)
        for thisComponent in trial1FourTrialsComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "trial1FourTrials"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = trial1FourTrialsClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stimulus1_2* updates
            if t >= 0.4 and stimulus1_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                stimulus1_2.tStart = t  # underestimates by a little under one frame
                stimulus1_2.frameNStart = frameN  # exact frame index
                stimulus1_2.setAutoDraw(True)
            
            # *responseCorr1_2* updates
            if t >= 0.4 and responseCorr1_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                responseCorr1_2.tStart = t  # underestimates by a little under one frame
                responseCorr1_2.frameNStart = frameN  # exact frame index
                responseCorr1_2.status = STARTED
                # AllowedKeys looks like a variable named `responseAllowedCorr`
                if not 'responseAllowedCorr' in locals():
                    logging.error('AllowedKeys variable `responseAllowedCorr` is not defined.')
                    core.quit()
                if not type(responseAllowedCorr) in [list, tuple, np.ndarray]:
                    if not isinstance(responseAllowedCorr, basestring):
                        logging.error('AllowedKeys variable `responseAllowedCorr` is not string- or list-like.')
                        core.quit()
                    elif not ',' in responseAllowedCorr: responseAllowedCorr = (responseAllowedCorr,)
                    else:  responseAllowedCorr = eval(responseAllowedCorr)
                # keyboard checking is just starting
                responseCorr1_2.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if responseCorr1_2.status == STARTED:
                theseKeys = event.getKeys(keyList=list(responseAllowedCorr))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if responseCorr1_2.keys == []:  # then this was the first keypress
                        responseCorr1_2.keys = theseKeys[0]  # just the first key pressed
                        responseCorr1_2.rt = responseCorr1_2.clock.getTime()
                        # was this 'correct'?
                        if (responseCorr1_2.keys == str(corrAns)) or (responseCorr1_2.keys == corrAns):
                            responseCorr1_2.corr = 1
                        else:
                            responseCorr1_2.corr = 0
                        # a response ends the routine
                        continueRoutine = False
            
            # *responseIncor1_2* updates
            if t >= 0.4 and responseIncor1_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                responseIncor1_2.tStart = t  # underestimates by a little under one frame
                responseIncor1_2.frameNStart = frameN  # exact frame index
                responseIncor1_2.status = STARTED
                # AllowedKeys looks like a variable named `responseAllowedIncorr`
                if not 'responseAllowedIncorr' in locals():
                    logging.error('AllowedKeys variable `responseAllowedIncorr` is not defined.')
                    core.quit()
                if not type(responseAllowedIncorr) in [list, tuple, np.ndarray]:
                    if not isinstance(responseAllowedIncorr, basestring):
                        logging.error('AllowedKeys variable `responseAllowedIncorr` is not string- or list-like.')
                        core.quit()
                    elif not ',' in responseAllowedIncorr: responseAllowedIncorr = (responseAllowedIncorr,)
                    else:  responseAllowedIncorr = eval(responseAllowedIncorr)
                # keyboard checking is just starting
                responseIncor1_2.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if responseIncor1_2.status == STARTED:
                theseKeys = event.getKeys(keyList=list(responseAllowedIncorr))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if responseIncor1_2.keys == []:  # then this was the first keypress
                        responseIncor1_2.keys = theseKeys[0]  # just the first key pressed
                        responseIncor1_2.rt = responseIncor1_2.clock.getTime()
            if len(responseIncor1_2.keys)<1:
                msg1=""
            else:
                msg1="X"
            
            # *accuracyFeedback1_2* updates
            if t >= 0.4 and accuracyFeedback1_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                accuracyFeedback1_2.tStart = t  # underestimates by a little under one frame
                accuracyFeedback1_2.frameNStart = frameN  # exact frame index
                accuracyFeedback1_2.setAutoDraw(True)
            if accuracyFeedback1_2.status == STARTED:  # only update if being drawn
                accuracyFeedback1_2.setText(msg1, log=False)
            
            # *target1_2* updates
            if t >= 0.0 and target1_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                target1_2.tStart = t  # underestimates by a little under one frame
                target1_2.frameNStart = frameN  # exact frame index
                target1_2.setAutoDraw(True)
            
            # *attribute1_2* updates
            if t >= 0.0 and attribute1_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                attribute1_2.tStart = t  # underestimates by a little under one frame
                attribute1_2.frameNStart = frameN  # exact frame index
                attribute1_2.setAutoDraw(True)
            
            # *or1_2* updates
            if t >= 0.0 and or1_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                or1_2.tStart = t  # underestimates by a little under one frame
                or1_2.frameNStart = frameN  # exact frame index
                or1_2.setAutoDraw(True)
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial1FourTrialsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "trial1FourTrials"-------
        for thisComponent in trial1FourTrialsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if responseCorr1_2.keys in ['', [], None]:  # No response was made
           responseCorr1_2.keys=None
           # was no response the correct answer?!
           if str(corrAns).lower() == 'none': responseCorr1_2.corr = 1  # correct non-response
           else: responseCorr1_2.corr = 0  # failed to respond (incorrectly)
        # store data for trial1Loop1FourTrials (TrialHandler)
        trial1Loop1FourTrials.addData('responseCorr1_2.keys',responseCorr1_2.keys)
        trial1Loop1FourTrials.addData('responseCorr1_2.corr', responseCorr1_2.corr)
        if responseCorr1_2.keys != None:  # we had a response
            trial1Loop1FourTrials.addData('responseCorr1_2.rt', responseCorr1_2.rt)
        # check responses
        if responseIncor1_2.keys in ['', [], None]:  # No response was made
           responseIncor1_2.keys=None
        # store data for trial1Loop1FourTrials (TrialHandler)
        trial1Loop1FourTrials.addData('responseIncor1_2.keys',responseIncor1_2.keys)
        if responseIncor1_2.keys != None:  # we had a response
            trial1Loop1FourTrials.addData('responseIncor1_2.rt', responseIncor1_2.rt)
        
        if trialsCounter >= 4:
            trial1Loop1FourTrials.finished = True
        # the Routine "trial1FourTrials" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trial1Loop1FourTrials'
    
    
    # set up handler to look after randomisation of conditions etc
    trial1Loop1 = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions('category&AttributeStimuli.xlsx'),
        seed=None, name='trial1Loop1')
    thisExp.addLoop(trial1Loop1)  # add the loop to the experiment
    thisTrial1Loop1 = trial1Loop1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrial1Loop1.rgb)
    if thisTrial1Loop1 != None:
        for paramName in thisTrial1Loop1.keys():
            exec(paramName + '= thisTrial1Loop1.' + paramName)
    
    for thisTrial1Loop1 in trial1Loop1:
        currentLoop = trial1Loop1
        # abbreviate parameter names if possible (e.g. rgb = thisTrial1Loop1.rgb)
        if thisTrial1Loop1 != None:
            for paramName in thisTrial1Loop1.keys():
                exec(paramName + '= thisTrial1Loop1.' + paramName)
        
        #------Prepare to start Routine "trial1"-------
        t = 0
        trial1Clock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        stimulus1.setColor(stimulusColour, colorSpace='rgb')
        stimulus1.setText(stimulusVariable1)
        responseCorr1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        responseCorr1.status = NOT_STARTED
        responseIncor1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        responseIncor1.status = NOT_STARTED
        
        target1.setText(target1Text)
        attribute1.setColor([1.000,1.000,-1.000], colorSpace='rgb')
        attribute1.setText(attributeText)
        # keep track of which components have finished
        trial1Components = []
        trial1Components.append(stimulus1)
        trial1Components.append(responseCorr1)
        trial1Components.append(responseIncor1)
        trial1Components.append(accuracyFeedback1)
        trial1Components.append(target1)
        trial1Components.append(attribute1)
        trial1Components.append(or1)
        for thisComponent in trial1Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "trial1"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = trial1Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stimulus1* updates
            if t >= 0.4 and stimulus1.status == NOT_STARTED:
                # keep track of start time/frame for later
                stimulus1.tStart = t  # underestimates by a little under one frame
                stimulus1.frameNStart = frameN  # exact frame index
                stimulus1.setAutoDraw(True)
            
            # *responseCorr1* updates
            if t >= 0.4 and responseCorr1.status == NOT_STARTED:
                # keep track of start time/frame for later
                responseCorr1.tStart = t  # underestimates by a little under one frame
                responseCorr1.frameNStart = frameN  # exact frame index
                responseCorr1.status = STARTED
                # AllowedKeys looks like a variable named `responseAllowedCorr`
                if not 'responseAllowedCorr' in locals():
                    logging.error('AllowedKeys variable `responseAllowedCorr` is not defined.')
                    core.quit()
                if not type(responseAllowedCorr) in [list, tuple, np.ndarray]:
                    if not isinstance(responseAllowedCorr, basestring):
                        logging.error('AllowedKeys variable `responseAllowedCorr` is not string- or list-like.')
                        core.quit()
                    elif not ',' in responseAllowedCorr: responseAllowedCorr = (responseAllowedCorr,)
                    else:  responseAllowedCorr = eval(responseAllowedCorr)
                # keyboard checking is just starting
                responseCorr1.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if responseCorr1.status == STARTED:
                theseKeys = event.getKeys(keyList=list(responseAllowedCorr))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if responseCorr1.keys == []:  # then this was the first keypress
                        responseCorr1.keys = theseKeys[0]  # just the first key pressed
                        responseCorr1.rt = responseCorr1.clock.getTime()
                        # was this 'correct'?
                        if (responseCorr1.keys == str(corrAns)) or (responseCorr1.keys == corrAns):
                            responseCorr1.corr = 1
                        else:
                            responseCorr1.corr = 0
                        # a response ends the routine
                        continueRoutine = False
            
            # *responseIncor1* updates
            if t >= 0.4 and responseIncor1.status == NOT_STARTED:
                # keep track of start time/frame for later
                responseIncor1.tStart = t  # underestimates by a little under one frame
                responseIncor1.frameNStart = frameN  # exact frame index
                responseIncor1.status = STARTED
                # AllowedKeys looks like a variable named `responseAllowedIncorr`
                if not 'responseAllowedIncorr' in locals():
                    logging.error('AllowedKeys variable `responseAllowedIncorr` is not defined.')
                    core.quit()
                if not type(responseAllowedIncorr) in [list, tuple, np.ndarray]:
                    if not isinstance(responseAllowedIncorr, basestring):
                        logging.error('AllowedKeys variable `responseAllowedIncorr` is not string- or list-like.')
                        core.quit()
                    elif not ',' in responseAllowedIncorr: responseAllowedIncorr = (responseAllowedIncorr,)
                    else:  responseAllowedIncorr = eval(responseAllowedIncorr)
                # keyboard checking is just starting
                responseIncor1.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if responseIncor1.status == STARTED:
                theseKeys = event.getKeys(keyList=list(responseAllowedIncorr))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if responseIncor1.keys == []:  # then this was the first keypress
                        responseIncor1.keys = theseKeys[0]  # just the first key pressed
                        responseIncor1.rt = responseIncor1.clock.getTime()
            if len(responseIncor1.keys)<1:
                msg1=""
            else:
                msg1="X"
            
            # *accuracyFeedback1* updates
            if t >= 0.4 and accuracyFeedback1.status == NOT_STARTED:
                # keep track of start time/frame for later
                accuracyFeedback1.tStart = t  # underestimates by a little under one frame
                accuracyFeedback1.frameNStart = frameN  # exact frame index
                accuracyFeedback1.setAutoDraw(True)
            if accuracyFeedback1.status == STARTED:  # only update if being drawn
                accuracyFeedback1.setText(msg1, log=False)
            
            # *target1* updates
            if t >= 0.0 and target1.status == NOT_STARTED:
                # keep track of start time/frame for later
                target1.tStart = t  # underestimates by a little under one frame
                target1.frameNStart = frameN  # exact frame index
                target1.setAutoDraw(True)
            
            # *attribute1* updates
            if t >= 0.0 and attribute1.status == NOT_STARTED:
                # keep track of start time/frame for later
                attribute1.tStart = t  # underestimates by a little under one frame
                attribute1.frameNStart = frameN  # exact frame index
                attribute1.setAutoDraw(True)
            
            # *or1* updates
            if t >= 0.0 and or1.status == NOT_STARTED:
                # keep track of start time/frame for later
                or1.tStart = t  # underestimates by a little under one frame
                or1.frameNStart = frameN  # exact frame index
                or1.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "trial1"-------
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if responseCorr1.keys in ['', [], None]:  # No response was made
           responseCorr1.keys=None
           # was no response the correct answer?!
           if str(corrAns).lower() == 'none': responseCorr1.corr = 1  # correct non-response
           else: responseCorr1.corr = 0  # failed to respond (incorrectly)
        # store data for trial1Loop1 (TrialHandler)
        trial1Loop1.addData('responseCorr1.keys',responseCorr1.keys)
        trial1Loop1.addData('responseCorr1.corr', responseCorr1.corr)
        if responseCorr1.keys != None:  # we had a response
            trial1Loop1.addData('responseCorr1.rt', responseCorr1.rt)
        # check responses
        if responseIncor1.keys in ['', [], None]:  # No response was made
           responseIncor1.keys=None
        # store data for trial1Loop1 (TrialHandler)
        trial1Loop1.addData('responseIncor1.keys',responseIncor1.keys)
        if responseIncor1.keys != None:  # we had a response
            trial1Loop1.addData('responseIncor1.rt', responseIncor1.rt)
        
        # the Routine "trial1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trial1Loop1'
    
    
    #------Prepare to start Routine "instructions2"-------
    t = 0
    instructions2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    contResponse2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    contResponse2.status = NOT_STARTED
    trialsCounter = 0
    # keep track of which components have finished
    instructions2Components = []
    instructions2Components.append(contResponse2)
    instructions2Components.append(category2Label)
    instructions2Components.append(category2Stimuli)
    instructions2Components.append(attributeLabel2)
    instructions2Components.append(attributeStimuli2)
    instructions2Components.append(orLabel2)
    instructions2Components.append(pressI2)
    instructions2Components.append(pressE2)
    instructions2Components.append(goFast2)
    instructions2Components.append(pressSpace2)
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "instructions2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = instructions2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *contResponse2* updates
        if t >= 0.0 and contResponse2.status == NOT_STARTED:
            # keep track of start time/frame for later
            contResponse2.tStart = t  # underestimates by a little under one frame
            contResponse2.frameNStart = frameN  # exact frame index
            contResponse2.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if contResponse2.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # *category2Label* updates
        if t >= 0.0 and category2Label.status == NOT_STARTED:
            # keep track of start time/frame for later
            category2Label.tStart = t  # underestimates by a little under one frame
            category2Label.frameNStart = frameN  # exact frame index
            category2Label.setAutoDraw(True)
        
        # *category2Stimuli* updates
        if t >= 0.0 and category2Stimuli.status == NOT_STARTED:
            # keep track of start time/frame for later
            category2Stimuli.tStart = t  # underestimates by a little under one frame
            category2Stimuli.frameNStart = frameN  # exact frame index
            category2Stimuli.setAutoDraw(True)
        
        # *attributeLabel2* updates
        if t >= 0.0 and attributeLabel2.status == NOT_STARTED:
            # keep track of start time/frame for later
            attributeLabel2.tStart = t  # underestimates by a little under one frame
            attributeLabel2.frameNStart = frameN  # exact frame index
            attributeLabel2.setAutoDraw(True)
        
        # *attributeStimuli2* updates
        if t >= 0.0 and attributeStimuli2.status == NOT_STARTED:
            # keep track of start time/frame for later
            attributeStimuli2.tStart = t  # underestimates by a little under one frame
            attributeStimuli2.frameNStart = frameN  # exact frame index
            attributeStimuli2.setAutoDraw(True)
        
        # *orLabel2* updates
        if t >= 0.0 and orLabel2.status == NOT_STARTED:
            # keep track of start time/frame for later
            orLabel2.tStart = t  # underestimates by a little under one frame
            orLabel2.frameNStart = frameN  # exact frame index
            orLabel2.setAutoDraw(True)
        
        # *pressI2* updates
        if t >= 0.0 and pressI2.status == NOT_STARTED:
            # keep track of start time/frame for later
            pressI2.tStart = t  # underestimates by a little under one frame
            pressI2.frameNStart = frameN  # exact frame index
            pressI2.setAutoDraw(True)
        
        # *pressE2* updates
        if t >= 0.0 and pressE2.status == NOT_STARTED:
            # keep track of start time/frame for later
            pressE2.tStart = t  # underestimates by a little under one frame
            pressE2.frameNStart = frameN  # exact frame index
            pressE2.setAutoDraw(True)
        
        # *goFast2* updates
        if t >= 0.0 and goFast2.status == NOT_STARTED:
            # keep track of start time/frame for later
            goFast2.tStart = t  # underestimates by a little under one frame
            goFast2.frameNStart = frameN  # exact frame index
            goFast2.setAutoDraw(True)
        
        # *pressSpace2* updates
        if t >= 0.0 and pressSpace2.status == NOT_STARTED:
            # keep track of start time/frame for later
            pressSpace2.tStart = t  # underestimates by a little under one frame
            pressSpace2.frameNStart = frameN  # exact frame index
            pressSpace2.setAutoDraw(True)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "instructions2"-------
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "instructions2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trial2Loop1FourTrials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions('categoryStimuli.xlsx'),
        seed=None, name='trial2Loop1FourTrials')
    thisExp.addLoop(trial2Loop1FourTrials)  # add the loop to the experiment
    thisTrial2Loop1FourTrial = trial2Loop1FourTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrial2Loop1FourTrial.rgb)
    if thisTrial2Loop1FourTrial != None:
        for paramName in thisTrial2Loop1FourTrial.keys():
            exec(paramName + '= thisTrial2Loop1FourTrial.' + paramName)
    
    for thisTrial2Loop1FourTrial in trial2Loop1FourTrials:
        currentLoop = trial2Loop1FourTrials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial2Loop1FourTrial.rgb)
        if thisTrial2Loop1FourTrial != None:
            for paramName in thisTrial2Loop1FourTrial.keys():
                exec(paramName + '= thisTrial2Loop1FourTrial.' + paramName)
        
        #------Prepare to start Routine "trial2FourTrials"-------
        t = 0
        trial2FourTrialsClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        stimulus2_2.setColor(stimulusColour, colorSpace='rgb')
        stimulus2_2.setText(stimulusVariable2)
        responseCorr2_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        responseCorr2_2.status = NOT_STARTED
        responseIncor2_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        responseIncor2_2.status = NOT_STARTED
        
        target2_2.setText(target2Text)
        attribute2_2.setColor([1.000,1.000,-1.000], colorSpace='rgb')
        attribute2_2.setText(attributeText)
        trialsCounter = trialsCounter + 1
        
        # keep track of which components have finished
        trial2FourTrialsComponents = []
        trial2FourTrialsComponents.append(stimulus2_2)
        trial2FourTrialsComponents.append(responseCorr2_2)
        trial2FourTrialsComponents.append(responseIncor2_2)
        trial2FourTrialsComponents.append(accuracyFeedback2_2)
        trial2FourTrialsComponents.append(target2_2)
        trial2FourTrialsComponents.append(attribute2_2)
        trial2FourTrialsComponents.append(or2_2)
        for thisComponent in trial2FourTrialsComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "trial2FourTrials"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = trial2FourTrialsClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stimulus2_2* updates
            if t >= 0.4 and stimulus2_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                stimulus2_2.tStart = t  # underestimates by a little under one frame
                stimulus2_2.frameNStart = frameN  # exact frame index
                stimulus2_2.setAutoDraw(True)
            
            # *responseCorr2_2* updates
            if t >= 0.4 and responseCorr2_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                responseCorr2_2.tStart = t  # underestimates by a little under one frame
                responseCorr2_2.frameNStart = frameN  # exact frame index
                responseCorr2_2.status = STARTED
                # AllowedKeys looks like a variable named `responseAllowedCorr`
                if not 'responseAllowedCorr' in locals():
                    logging.error('AllowedKeys variable `responseAllowedCorr` is not defined.')
                    core.quit()
                if not type(responseAllowedCorr) in [list, tuple, np.ndarray]:
                    if not isinstance(responseAllowedCorr, basestring):
                        logging.error('AllowedKeys variable `responseAllowedCorr` is not string- or list-like.')
                        core.quit()
                    elif not ',' in responseAllowedCorr: responseAllowedCorr = (responseAllowedCorr,)
                    else:  responseAllowedCorr = eval(responseAllowedCorr)
                # keyboard checking is just starting
                responseCorr2_2.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if responseCorr2_2.status == STARTED:
                theseKeys = event.getKeys(keyList=list(responseAllowedCorr))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if responseCorr2_2.keys == []:  # then this was the first keypress
                        responseCorr2_2.keys = theseKeys[0]  # just the first key pressed
                        responseCorr2_2.rt = responseCorr2_2.clock.getTime()
                        # was this 'correct'?
                        if (responseCorr2_2.keys == str(corrAns)) or (responseCorr2_2.keys == corrAns):
                            responseCorr2_2.corr = 1
                        else:
                            responseCorr2_2.corr = 0
                        # a response ends the routine
                        continueRoutine = False
            
            # *responseIncor2_2* updates
            if t >= 0.4 and responseIncor2_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                responseIncor2_2.tStart = t  # underestimates by a little under one frame
                responseIncor2_2.frameNStart = frameN  # exact frame index
                responseIncor2_2.status = STARTED
                # AllowedKeys looks like a variable named `responseAllowedIncorr`
                if not 'responseAllowedIncorr' in locals():
                    logging.error('AllowedKeys variable `responseAllowedIncorr` is not defined.')
                    core.quit()
                if not type(responseAllowedIncorr) in [list, tuple, np.ndarray]:
                    if not isinstance(responseAllowedIncorr, basestring):
                        logging.error('AllowedKeys variable `responseAllowedIncorr` is not string- or list-like.')
                        core.quit()
                    elif not ',' in responseAllowedIncorr: responseAllowedIncorr = (responseAllowedIncorr,)
                    else:  responseAllowedIncorr = eval(responseAllowedIncorr)
                # keyboard checking is just starting
                responseIncor2_2.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if responseIncor2_2.status == STARTED:
                theseKeys = event.getKeys(keyList=list(responseAllowedIncorr))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if responseIncor2_2.keys == []:  # then this was the first keypress
                        responseIncor2_2.keys = theseKeys[0]  # just the first key pressed
                        responseIncor2_2.rt = responseIncor2_2.clock.getTime()
            if len(responseIncor2_2.keys)<1:
                msg2=""
            else:
                msg2="X"
            
            # *accuracyFeedback2_2* updates
            if t >= 0.4 and accuracyFeedback2_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                accuracyFeedback2_2.tStart = t  # underestimates by a little under one frame
                accuracyFeedback2_2.frameNStart = frameN  # exact frame index
                accuracyFeedback2_2.setAutoDraw(True)
            if accuracyFeedback2_2.status == STARTED:  # only update if being drawn
                accuracyFeedback2_2.setText(msg2, log=False)
            
            # *target2_2* updates
            if t >= 0.0 and target2_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                target2_2.tStart = t  # underestimates by a little under one frame
                target2_2.frameNStart = frameN  # exact frame index
                target2_2.setAutoDraw(True)
            
            # *attribute2_2* updates
            if t >= 0.0 and attribute2_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                attribute2_2.tStart = t  # underestimates by a little under one frame
                attribute2_2.frameNStart = frameN  # exact frame index
                attribute2_2.setAutoDraw(True)
            
            # *or2_2* updates
            if t >= 0.0 and or2_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                or2_2.tStart = t  # underestimates by a little under one frame
                or2_2.frameNStart = frameN  # exact frame index
                or2_2.setAutoDraw(True)
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial2FourTrialsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "trial2FourTrials"-------
        for thisComponent in trial2FourTrialsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if responseCorr2_2.keys in ['', [], None]:  # No response was made
           responseCorr2_2.keys=None
           # was no response the correct answer?!
           if str(corrAns).lower() == 'none': responseCorr2_2.corr = 1  # correct non-response
           else: responseCorr2_2.corr = 0  # failed to respond (incorrectly)
        # store data for trial2Loop1FourTrials (TrialHandler)
        trial2Loop1FourTrials.addData('responseCorr2_2.keys',responseCorr2_2.keys)
        trial2Loop1FourTrials.addData('responseCorr2_2.corr', responseCorr2_2.corr)
        if responseCorr2_2.keys != None:  # we had a response
            trial2Loop1FourTrials.addData('responseCorr2_2.rt', responseCorr2_2.rt)
        # check responses
        if responseIncor2_2.keys in ['', [], None]:  # No response was made
           responseIncor2_2.keys=None
        # store data for trial2Loop1FourTrials (TrialHandler)
        trial2Loop1FourTrials.addData('responseIncor2_2.keys',responseIncor2_2.keys)
        if responseIncor2_2.keys != None:  # we had a response
            trial2Loop1FourTrials.addData('responseIncor2_2.rt', responseIncor2_2.rt)
        
        if trialsCounter >= 4:
            trial2Loop1FourTrials.finished = True
        # the Routine "trial2FourTrials" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trial2Loop1FourTrials'
    
    
    # set up handler to look after randomisation of conditions etc
    trial2Loop1 = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions('category&AttributeStimuli.xlsx'),
        seed=None, name='trial2Loop1')
    thisExp.addLoop(trial2Loop1)  # add the loop to the experiment
    thisTrial2Loop1 = trial2Loop1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrial2Loop1.rgb)
    if thisTrial2Loop1 != None:
        for paramName in thisTrial2Loop1.keys():
            exec(paramName + '= thisTrial2Loop1.' + paramName)
    
    for thisTrial2Loop1 in trial2Loop1:
        currentLoop = trial2Loop1
        # abbreviate parameter names if possible (e.g. rgb = thisTrial2Loop1.rgb)
        if thisTrial2Loop1 != None:
            for paramName in thisTrial2Loop1.keys():
                exec(paramName + '= thisTrial2Loop1.' + paramName)
        
        #------Prepare to start Routine "trial2"-------
        t = 0
        trial2Clock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        stimulus2.setColor(stimulusColour, colorSpace='rgb')
        stimulus2.setText(stimulusVariable2)
        responseCorr2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        responseCorr2.status = NOT_STARTED
        responseIncor2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        responseIncor2.status = NOT_STARTED
        
        target2.setText(target2Text)
        attribute2.setColor([1.000,1.000,-1.000], colorSpace='rgb')
        attribute2.setText(attributeText)
        # keep track of which components have finished
        trial2Components = []
        trial2Components.append(stimulus2)
        trial2Components.append(responseCorr2)
        trial2Components.append(responseIncor2)
        trial2Components.append(accuracyFeedback2)
        trial2Components.append(target2)
        trial2Components.append(attribute2)
        trial2Components.append(or2)
        for thisComponent in trial2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "trial2"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = trial2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stimulus2* updates
            if t >= 0.4 and stimulus2.status == NOT_STARTED:
                # keep track of start time/frame for later
                stimulus2.tStart = t  # underestimates by a little under one frame
                stimulus2.frameNStart = frameN  # exact frame index
                stimulus2.setAutoDraw(True)
            
            # *responseCorr2* updates
            if t >= 0.4 and responseCorr2.status == NOT_STARTED:
                # keep track of start time/frame for later
                responseCorr2.tStart = t  # underestimates by a little under one frame
                responseCorr2.frameNStart = frameN  # exact frame index
                responseCorr2.status = STARTED
                # AllowedKeys looks like a variable named `responseAllowedCorr`
                if not 'responseAllowedCorr' in locals():
                    logging.error('AllowedKeys variable `responseAllowedCorr` is not defined.')
                    core.quit()
                if not type(responseAllowedCorr) in [list, tuple, np.ndarray]:
                    if not isinstance(responseAllowedCorr, basestring):
                        logging.error('AllowedKeys variable `responseAllowedCorr` is not string- or list-like.')
                        core.quit()
                    elif not ',' in responseAllowedCorr: responseAllowedCorr = (responseAllowedCorr,)
                    else:  responseAllowedCorr = eval(responseAllowedCorr)
                # keyboard checking is just starting
                responseCorr2.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if responseCorr2.status == STARTED:
                theseKeys = event.getKeys(keyList=list(responseAllowedCorr))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if responseCorr2.keys == []:  # then this was the first keypress
                        responseCorr2.keys = theseKeys[0]  # just the first key pressed
                        responseCorr2.rt = responseCorr2.clock.getTime()
                        # was this 'correct'?
                        if (responseCorr2.keys == str(corrAns)) or (responseCorr2.keys == corrAns):
                            responseCorr2.corr = 1
                        else:
                            responseCorr2.corr = 0
                        # a response ends the routine
                        continueRoutine = False
            
            # *responseIncor2* updates
            if t >= 0.4 and responseIncor2.status == NOT_STARTED:
                # keep track of start time/frame for later
                responseIncor2.tStart = t  # underestimates by a little under one frame
                responseIncor2.frameNStart = frameN  # exact frame index
                responseIncor2.status = STARTED
                # AllowedKeys looks like a variable named `responseAllowedIncorr`
                if not 'responseAllowedIncorr' in locals():
                    logging.error('AllowedKeys variable `responseAllowedIncorr` is not defined.')
                    core.quit()
                if not type(responseAllowedIncorr) in [list, tuple, np.ndarray]:
                    if not isinstance(responseAllowedIncorr, basestring):
                        logging.error('AllowedKeys variable `responseAllowedIncorr` is not string- or list-like.')
                        core.quit()
                    elif not ',' in responseAllowedIncorr: responseAllowedIncorr = (responseAllowedIncorr,)
                    else:  responseAllowedIncorr = eval(responseAllowedIncorr)
                # keyboard checking is just starting
                responseIncor2.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if responseIncor2.status == STARTED:
                theseKeys = event.getKeys(keyList=list(responseAllowedIncorr))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if responseIncor2.keys == []:  # then this was the first keypress
                        responseIncor2.keys = theseKeys[0]  # just the first key pressed
                        responseIncor2.rt = responseIncor2.clock.getTime()
            if len(responseIncor2.keys)<1:
                msg2=""
            else:
                msg2="X"
            
            # *accuracyFeedback2* updates
            if t >= 0.4 and accuracyFeedback2.status == NOT_STARTED:
                # keep track of start time/frame for later
                accuracyFeedback2.tStart = t  # underestimates by a little under one frame
                accuracyFeedback2.frameNStart = frameN  # exact frame index
                accuracyFeedback2.setAutoDraw(True)
            if accuracyFeedback2.status == STARTED:  # only update if being drawn
                accuracyFeedback2.setText(msg2, log=False)
            
            # *target2* updates
            if t >= 0.0 and target2.status == NOT_STARTED:
                # keep track of start time/frame for later
                target2.tStart = t  # underestimates by a little under one frame
                target2.frameNStart = frameN  # exact frame index
                target2.setAutoDraw(True)
            
            # *attribute2* updates
            if t >= 0.0 and attribute2.status == NOT_STARTED:
                # keep track of start time/frame for later
                attribute2.tStart = t  # underestimates by a little under one frame
                attribute2.frameNStart = frameN  # exact frame index
                attribute2.setAutoDraw(True)
            
            # *or2* updates
            if t >= 0.0 and or2.status == NOT_STARTED:
                # keep track of start time/frame for later
                or2.tStart = t  # underestimates by a little under one frame
                or2.frameNStart = frameN  # exact frame index
                or2.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "trial2"-------
        for thisComponent in trial2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if responseCorr2.keys in ['', [], None]:  # No response was made
           responseCorr2.keys=None
           # was no response the correct answer?!
           if str(corrAns).lower() == 'none': responseCorr2.corr = 1  # correct non-response
           else: responseCorr2.corr = 0  # failed to respond (incorrectly)
        # store data for trial2Loop1 (TrialHandler)
        trial2Loop1.addData('responseCorr2.keys',responseCorr2.keys)
        trial2Loop1.addData('responseCorr2.corr', responseCorr2.corr)
        if responseCorr2.keys != None:  # we had a response
            trial2Loop1.addData('responseCorr2.rt', responseCorr2.rt)
        # check responses
        if responseIncor2.keys in ['', [], None]:  # No response was made
           responseIncor2.keys=None
        # store data for trial2Loop1 (TrialHandler)
        trial2Loop1.addData('responseIncor2.keys',responseIncor2.keys)
        if responseIncor2.keys != None:  # we had a response
            trial2Loop1.addData('responseIncor2.rt', responseIncor2.rt)
        
        # the Routine "trial2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trial2Loop1'
    
    thisExp.nextEntry()
    
# completed 2 repeats of 'repeatBlockPairLoop'


#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
endResponse = event.BuilderKeyResponse()  # create an object of type KeyResponse
endResponse.status = NOT_STARTED
# keep track of which components have finished
endComponents = []
endComponents.append(endMessage)
endComponents.append(endResponse)
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endMessage* updates
    if t >= 0 and endMessage.status == NOT_STARTED:
        # keep track of start time/frame for later
        endMessage.tStart = t  # underestimates by a little under one frame
        endMessage.frameNStart = frameN  # exact frame index
        endMessage.setAutoDraw(True)
    
    # *endResponse* updates
    if t >= 0.0 and endResponse.status == NOT_STARTED:
        # keep track of start time/frame for later
        endResponse.tStart = t  # underestimates by a little under one frame
        endResponse.frameNStart = frameN  # exact frame index
        endResponse.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if endResponse.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()








win.close()
core.quit()
