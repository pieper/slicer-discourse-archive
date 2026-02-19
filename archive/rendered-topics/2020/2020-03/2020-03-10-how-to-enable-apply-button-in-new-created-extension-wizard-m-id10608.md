---
topic_id: 10608
title: "How To Enable Apply Button In New Created Extension Wizard M"
date: 2020-03-10
url: https://discourse.slicer.org/t/10608
---

# How to enable apply button in new created Extension Wizard module?

**Topic ID**: 10608
**Date**: 2020-03-10
**URL**: https://discourse.slicer.org/t/how-to-enable-apply-button-in-new-created-extension-wizard-module/10608

---

## Post #1 by @Illusion (2020-03-10 04:17 UTC)

<p>Hello,</p>
<p>I am new in Slicer programming.</p>
<p>Created a module using extension wizard, however, the self.applyButton in Widget class is always disabled. I use PyCharm to debug, and in the function</p>
<p>‘’’<br>
def onSelect(self):<br>
           self.applyButton.enabled = self.inputSelector.currentNode() and self.outputSelector.currentNode()<br>
‘’’</p>
<p>when a new volume is loaded, the function onSelect is triggered, both inputSelector and outputSelector are not null. However, I could never see the applyButton enabled.</p>
<p>Why couldn’t the applyButton be enabled?<br>
How should I enable it? Or should I change the code?</p>
<p>Thank you very much!</p>

---

## Post #2 by @lassoan (2020-03-10 04:49 UTC)

<p>I would recommend to use the latest <a href="https://github.com/Slicer/Slicer/blob/master/Utilities/Templates/Modules/ScriptedDesigner/TemplateKey.py">“scripteddesigner” module template</a>. GUI state updates should be more clear now. If you have any questions about this latest template then let us know.</p>
<p>If you want to keep using the old template then adding a breakpoint in PyCharm execute the code step-by-step is a good way to understand what your code does (and why it is not the same what you expect).</p>

---

## Post #3 by @Illusion (2020-03-10 17:46 UTC)

<p>Hi Iassoan,</p>
<p>The latest template you recommended using UI framework seems even harder to understand. Any resource as a tutorial showing how to build a customerized template?</p>
<p>I am more familiar with qt commands without using UI, do you have any tutorial explanation for the template without UI, please?</p>
<p>Thank you very much!</p>

---

## Post #4 by @lassoan (2020-03-10 18:11 UTC)

<aside class="quote no-group quote-modified" data-username="Illusion" data-post="3" data-topic="10608">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/e19b73/48.png" class="avatar"> Illusion:</div>
<blockquote>
<p>The latest template you recommended using UI framework seems even harder to understand, with no comments as explanation at all.</p>
</blockquote>
</aside>
<p>Maybe you have checked an earlier version? <a href="https://github.com/Slicer/Slicer/blob/master/Utilities/Templates/Modules/ScriptedDesigner/TemplateKey.py">ScriptedDesigner template</a> was already quite well documented, but I added even more comments. If anything is still unclear then let me know.</p>
<p>We have found that using a .ui file for creating GUI makes the GUI easier to design and the code easier to debug and maintain. If you are not familiar with it then check out <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">this tutorial</a>.</p>

---

## Post #5 by @Illusion (2020-03-10 19:40 UTC)

<p>Hi Iassoan,</p>
<p>In the extension wizard template, the run function in Logic class was commented as “run the actual algorithm”, but there is not much explanation about how the thresholded output volume was calculated:</p>
<hr>
<pre><code># Compute the thresholded output volume using the Threshold Scalar Volume CLI module
cliParams = {'InputVolume': inputVolume.GetID(), 'OutputVolume': outputVolume.GetID(), 'ThresholdValue' : imageThreshold, 'ThresholdType' : 'Above'}
cliNode = slicer.cli.run(slicer.modules.thresholdscalarvolume, None, cliParams, wait_for_completion=True)
</code></pre>
<hr>
<p>where I was not able to extract any useful information from function slicer.cli.run(…)  <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=9" title=":sweat_smile:" class="emoji" alt=":sweat_smile:"></p>
<p>Could you please explain a little about how slicer.modules.thresholdscalarvolume applied the algorithm? And what exactly is the algorithm?</p>
<p>Thank you very much!</p>

---

## Post #6 by @lassoan (2020-03-10 22:39 UTC)

<p>The example shows how to run a CLI module from Python. See more information about CLI modules in general in the Slicer developer tutorials, and more details about how to run them and how to get their input/output parameters are available <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python">here</a>. Source code of CLI modules bundled with Slicer are available <a href="https://github.com/Slicer/Slicer/tree/master/Modules/CLI">here</a>.</p>
<p>You can run any other processing using VTK, SimpleITK, numpy, various Slicer modules provided by extensions, and any Python packages. See a variety of examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a>.</p>

---

## Post #7 by @Illusion (2020-03-10 22:47 UTC)

<aside class="quote no-group" data-username="Illusion" data-post="5" data-topic="10608">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/e19b73/48.png" class="avatar"> Illusion:</div>
<blockquote>
<p>thresholdscalarvolume</p>
</blockquote>
</aside>
<p>Hi Iassoan,</p>
<p>Thank you for providing the link to the code of thresholdscalarvolume module!</p>
<p>Is the link below where I should investigate for the algorithm of ThresholdScalarVolume?<br>
It seems that the module does not contain any comments, and I was not able to find out how the threshold was applied. <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=15" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"></p>
<hr>
<h2><a name="p-37114-httpsgithubcomslicerslicerblobmastermodulesclithresholdscalarvolumethresholdscalarvolumecxx-1" class="anchor" href="#p-37114-httpsgithubcomslicerslicerblobmastermodulesclithresholdscalarvolumethresholdscalarvolumecxx-1" aria-label="Heading link"></a><a href="https://github.com/Slicer/Slicer/blob/master/Modules/CLI/ThresholdScalarVolume/ThresholdScalarVolume.cxx" class="inline-onebox" rel="noopener nofollow ugc">Slicer/Modules/CLI/ThresholdScalarVolume/ThresholdScalarVolume.cxx at main · Slicer/Slicer · GitHub</a></h2>
<p>Would you be able to let me know how to locate the function that actually applied the algorithm of ThresholdScalarVolume, please?</p>

---

## Post #8 by @lassoan (2020-03-11 12:21 UTC)

<p>Most CLI modules use ITK filters to process data. You can find documentation, examples, and source code by searching for the filter name on the web (e.g., itk::ThresholdImageFilter).<br>
You can <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Running_an_ITK_filter_in_Python_using_SimpleITK">run ITK filters directly in Python using SimpleITK</a>, which is bundled with Slicer. You can also implement trivial operations, such as image thresholding using <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Modify_voxels_in_a_volume">numpy</a>. These are all described in the PerkLab Slicer programming tutorial that I linked above.</p>

---

## Post #9 by @Saima (2021-06-08 06:22 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="10608">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>you have any questions about this latest template then let us know.</p>
</blockquote>
</aside>
<p>Hi Andras,<br>
Why this scripteddesigner not available in new slicer versions. when I create an extension it shows me</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/880615f9650f829346126c189ae4bddf04a8535b.png" alt="image" data-base62-sha1="jpjYrelSO8x3hS8QQ7m9hmgOQgX" width="454" height="374"></p>
<p>it does give me a scripted designer in the list.</p>
<p>Thank you</p>

---

## Post #10 by @lassoan (2021-06-08 14:51 UTC)

<p>The old “scripted” template was removed and “scripteddesigner” template was renamed to “scripted”.</p>

---
