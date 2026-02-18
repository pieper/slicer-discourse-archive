# Play custom sound with Breach Warning?

**Topic ID**: 36790
**Date**: 2024-06-14
**URL**: https://discourse.slicer.org/t/play-custom-sound-with-breach-warning/36790

---

## Post #1 by @mikebind (2024-06-14 18:19 UTC)

<p>For trainee feedback when using a flexible scope with a electromagnetically tracked tip on a 3D printed mannequin airway, we would like to implement playing of sounds when certain areas are entered or touched.  Slicer IGT’s BreachWarning module already implements almost everything we need!  However, we would like to play different sounds in different areas, and as far as I can tell, BreachWarning only has a single, hard-coded sound which can be triggered, in “alarm.wav”.  Is there any way to change the file which is played?  Preferably from python?  I realize I can probably replace the contents of the alarm.wav file with whatever sound we want, but I don’t see a way to have two different sounds triggered depending on location.  We would like to have one area be a verbal “Ow”, another area a cough, and perhaps a third area with a gagging sound. I did see the Open Sound Control extension, but that seems focused on interactively generating sounds from a visual programming sound generation framework, which seems much more complicated than what we want to accomplish, which is just play different sound files for different Breach Warning nodes. Is this possible?</p>

---

## Post #2 by @mikebind (2024-06-14 18:27 UTC)

<p>Could I observe a Breach Warning node and trigger playing my own sound based on a broadcast event?</p>

---

## Post #3 by @mikebind (2024-06-14 23:25 UTC)

<p>I was able to get this working in a basic way by observing vtk.vtkCommand.ModifiedEvent events on a vtkMRMLBreachWarningNode. However, it seems to be significantly slowing the refresh rate of visualizations; is there a less common event I could observe?  Something that is fired off only when the tool is inside the model?</p>

---

## Post #4 by @lassoan (2024-06-15 12:11 UTC)

<p>Performing a very quick check in the observer should not slow down the GUI updates. Can you copy here the code that is executed by the observer?</p>
<p>Anyway, you can add an observer to the associated model node’s display node. The color is only changed when the breach starts or ends, which are rare events.</p>

---

## Post #5 by @mikebind (2024-06-20 19:19 UTC)

<p>Thanks for the advice, observing the model node instead of the breach warning node should work fine, I will try that.</p>
<p>Here is the code which was leading to slower refresh rates:</p>
<pre><code class="lang-auto">    def setUpBreachSound(self,watchedModel,tipTransform,breachDistanceThresh=0.0,wavFilePath=None):
        """ Needs documentation...
        """
        breachWarningNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLBreachWarningNode')
        breachWarningNode.SetAndObserveToolTransformNodeId(tipTransform.GetID())
        breachWarningNode.SetAndObserveWatchedModelNodeID(watchedModel.GetID())
        breachWarningNode.SetWarningDistanceMM(breachDistanceThresh)
        breachWarningNode.SetPlayWarningSound(False) # wav file should be played rather than beep
        # Set up observer
        callback = lambda unused1, unused2: self.breachWarningNodeModified(breachWarningNode, wavFilePath)
        # The lambda is needed because the callback is going to get two extra inputs which 
        # aren't needed or used
        observerTag = breachWarningNode.AddObserver(vtk.vtkCommand.ModifiedEvent, callback)
        return breachWarningNode, observerTag
        
    def breachWarningNodeModified(self, breachWarningNode, wavFilePath):
        """ This callback is called whenever breachWarningNode is modified 
        (which is going to be all the time when the postions are being updated).
        This function's purpose is to check whether a sound should be played
        or whether to just return. 
        """
        #Note: IsToolTipInsideModel includes the breach distance threshold
        if breachWarningNode.IsToolTipInsideModel():
            self.playWavSound(wavFilePath)

    def playWavSound(self,wavFilePath=None):
        """ Play a sound from a .wav file. 
        NOTE: mp3 files are not playable because
        QSound can't handle them, convert to .wav
        first or use QMultiMedia or maybe QSoundEffect
        or something like that.
        """
        if wavFilePath is None:
            wavFilePath = r"C:\Users\mbinds\Downloads\cough1.wav"

        qt.QSound.play(wavFilePath)
</code></pre>

---

## Post #6 by @lassoan (2024-06-20 19:33 UTC)

<p>Thanks for the information. The issue is here:</p>
<aside class="quote no-group" data-username="mikebind" data-post="5" data-topic="36790">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<pre><code class="lang-auto">if breachWarningNode.IsToolTipInsideModel():
            self.playWavSound(wavFilePath)
</code></pre>
</blockquote>
</aside>
<p>This code can start playing a sound file dozens of times per second. Reading and playing a sound file, initializing resources, and then send the signal to the hardware are all very heavy operations, so they indeed slow down the computer.</p>
<p>The most important thing is to only start playing the sound once, each time the tool goes into the region of interest (and not continuously, dozens of times per second). A further significant optimization would be to create a single <code>QSoundEffect</code> object and call its <code>play()</code> method each time the tool gets into the region of interest.</p>

---

## Post #7 by @mikebind (2024-06-20 21:47 UTC)

<p>Thanks, yes, I know further optimization will be needed to avoid starting the sound multiple times, but I had noticed the slowdown after initiating the observations and while no sounds were being triggered.  Thanks for the suggestion to create a single QSoundEffect resource up front, I will do that. I think observing the model node instead of the breach warning node should work to sidestep the slowdown issues.  It looks like QSoundEffect has an isPlaying() function which should also be useful for aborting sound restarts too soon.</p>

---

## Post #8 by @lassoan (2024-06-21 19:26 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="7" data-topic="36790">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>I had noticed the slowdown after initiating the observations and while no sounds were being triggered</p>
</blockquote>
</aside>
<p>Slowdown introduced by a single observer should not be noticeable if the callback function does not do anything computationally intensive. Maybe you ended up having many observers because you did not remove the observer or there is something else going on. But since the display node rarely changes anyway, we probably don’t need to investigate this any further.</p>
<p>Of course we could also make the sound configurable (e.g., by adding a get/set method for the QSoundEffect), but since for complex cases I would recommend using the SoundControl extension anyway (so that it can dynamically change the sound feedback, for example pitch or any other propery, stereo location, etc.), it may not worth the time.</p>

---
