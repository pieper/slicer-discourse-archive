---
topic_id: 2743
title: "Use Existing Slicer Modules With Python And Cli"
date: 2018-05-01
url: https://discourse.slicer.org/t/2743
---

# Use existing slicer modules with python and cli

**Topic ID**: 2743
**Date**: 2018-05-01
**URL**: https://discourse.slicer.org/t/use-existing-slicer-modules-with-python-and-cli/2743

---

## Post #1 by @hadasara (2018-05-01 11:48 UTC)

<p>Hi,<br>
I followed this tutorial on how to use existing modules in slicer through cli library:<br>
            <iframe width="480" height="360" src="https://www.youtube.com/embed/lK_p954iKZM?feature=oembed&amp;wmode=opaque&amp;list=PLJWCUXz3GeAfmYLiFcKus_c0jcsMnVsgb" frameborder="0" allowfullscreen="" seamless="seamless" sandbox="allow-same-origin allow-scripts allow-forms allow-popups allow-popups-to-escape-sandbox allow-presentation">
            </iframe>
</p>
<p>It sounds not bad (considering my understanding in cli is close to 0…)<br>
Anyway, since I want to use registration module (such as BRAINSfit) I’d like to have the option to cancel the operation after running it. but the cli cancel command is not implemented yet in the cli.py file that I’ve found.</p>
<p>so my questions:</p>
<ol>
<li>Is using slicer.cli is a good way execute existing modules proggramatically? If not- what is?</li>
<li>How can I cancel the running process with cli?</li>
</ol>
<p>Thanks!</p>
<p>Here is part of the code- the apply btton, executing the add Scalar Volume module (but can’t stop in the middle):</p>
<pre><code>   def onApplyButton(self):

        # allow cancel the process
        if self.InProgress:
            self.InProgress = False
            self.abortRequested = True
            raise ValueError("User requested cancel.")
            # self.cliNode.cancel() # not implemented
            self.applyutton.text = "Cancelling..."
            self.applyButton.enabled = False
            return

        self.InProgress = True
        self.applyButton.text = "Cancel"

        fixedImage  = self.fixedSelector.currentNode()
        movingImage = self.moveImgSelector.currentNode()
        outputImage = self.outputSelector.currentNode()

        if self.registratoinMethod == 'addScalarVolumes':
          moduleVar = slicer.modules.addscalarvolumes
          parameters = {}
          parameters["inputVolume1"] = fixedImage.GetID()
          parameters["inputVolume2"] = movingImage.GetID()
          parameters["outputVolume"] = outputImage.GetID()
          parameters["interpolation order"] = 0

        # get the module as object
        slicer.app.processEvents()
        self.cliNode = slicer.cli.run(moduleVar,None, parameters)
        print self.cliNode.cancel.
        self.bar.setCommandLineModuleNode(self.cliNode)

    # logic.run(self.fixedSelector.currentNode(),
        #           self.outputSelector.currentNode())
        # logic.run(fixedImage,movingImage,outputImage)

        # make the output volume appear in all the slice views
        slicer.util.setSliceViewerLayers(
            background=outputImage)</code></pre>

---

## Post #2 by @pieper (2018-05-01 13:18 UTC)

<ol>
<li>
<p>Yes</p>
</li>
<li>
<p>Did you try calling <code>self.cliNode.Cancel()</code>?  (that should probably be added to cli.py)</p>
</li>
</ol>

---

## Post #3 by @hadasara (2018-05-01 14:40 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="2743">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>self.cliNode.Cancel()</p>
</blockquote>
</aside>
<p>Hi, thanks! followed your suggestion- I did, but it didn’t work.<br>
begginner question- maybe there is a way to access the cancel of the module itself? (the cancel button exist in some modules)</p>

---

## Post #4 by @pieper (2018-05-01 15:30 UTC)

<p>Are you sure it didn’t work?  In your example code you have <code>cancel</code> but the method is <code>Cancel</code> with a capital <code>C</code>.  Calling <code>Cancel</code> should be the same as clicking the Cancel button on CLI interface widget.</p>

---

## Post #5 by @hadasara (2018-05-01 15:43 UTC)

<p>Thanks!! This fixed the problem!!<br>
I changed it to:</p>
<p>if self.InProgress:<br>
self.InProgress = False<br>
self.abortRequested = True<br>
self.cliNode.Cancel()<br>
self.applyButton.text = “Cancelling…”<br>
self.applyButton.enabled = False<br>
return<br>
now it cancel the progress.</p>
<p>Could you help me with another question?</p>
<ol>
<li>
<p>Is there a way to make something happen after the process is over? like change the name of the botton after it finishes.</p>
</li>
<li>
<p>How can I get through the cli the log, that is ussualy apear in the consol window while running the algorithm with the original loadable module?</p>
</li>
</ol>
<p>I couldn’t find an explanation here:<br>
<a href="https://www.slicer.org/wiki/Documentation/4.1/Modules/BRAINSFit" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.1/Modules/BRAINSFit</a></p>

---

## Post #6 by @pieper (2018-05-01 16:36 UTC)

<p>Great - glad that worked.</p>
<p>If you observe events from the cliNode you can tell what state the process is in and react accordingly.  You can review this documentation with the printStatus example:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python</a></p>
<p>Also to get the log info you can call <code>cliNode.GetOutputText()</code> and <code>cliNode.GetErrorText()</code></p>
<p>(I just updated the wiki with this info).</p>

---
