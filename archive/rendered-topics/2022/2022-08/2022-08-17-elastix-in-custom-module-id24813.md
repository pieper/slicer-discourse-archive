# Elastix in custom module

**Topic ID**: 24813
**Date**: 2022-08-17
**URL**: https://discourse.slicer.org/t/elastix-in-custom-module/24813

---

## Post #1 by @Vincebisca (2022-08-17 17:48 UTC)

<p>Hello,</p>
<p>I want to implement BSpline registration in a custom module in a seamless way for the user. For the registration I want to use Elastix with the “Generic (all)” preset.</p>
<p>I imported Elastix logic and used ElastixLogic.registerVolumes. I linked it to a Push Button to trigger the registration. My current code is :</p>
<p>def onRegistrationPushed(self):</p>
<pre><code class="lang-auto">FixedVolume = self.ui.SeqFixeSelector.currentNode()
MovingVolume = self.ui.SeqVariableSelector.currentNode()
parameters = "Parameters_BSpline.txt"
Transform = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLBSplineTransformNode")
volumesLogic = slicer.modules.volumes.logic()
OutputVolume = volumesLogic.CloneVolume(slicer.mrmlScene, MovingVolume, MovingVolume.GetName() + '_Registered' )

ElastixLogic.registerVolumes(self,FixedVolume, MovingVolume,parameters,OutputVolume, Transform)
</code></pre>
<p>However, when I tried to run it in 3DSlicer with 2 image sequences, it gave the error :</p>
<p>AttributeError: ‘GemSegmentWidget’ object has no attribute ‘createTempDirectory’</p>
<p>GemSegment is my module’s name. Digging a bit I saw that createTempDirectory is a function from Elastix.py, but then I don’t understand why it doesn’t search for it there. I tried to integrate createTempDirectory to my module’s .py file but it just moved the problem upwards, asking for the getTempDirectoryBase function.</p>
<p>If someone can help me understand how to properly use Elastix in my module I would be very glad ! Thank you !</p>

---

## Post #2 by @Sam_Horvath (2022-08-18 15:44 UTC)

<p>Hi, you need to create an instance i.e. <code>ElastixLogic()</code> rather than <code>ElastixLogic</code></p>
<p>so</p>
<pre><code class="lang-auto">elastixLogic = ElastixLogic()
elastixLogic.registerVolumes(FixedVolume, MovingVolume,parameters,OutputVolume, Transform)
</code></pre>
<p>See: <a href="https://github.com/lassoan/SlicerElastix/blob/3e9ef490ee6a6f901daa3280af112950f6af13ec/Elastix/Elastix.py#L939" class="inline-onebox">SlicerElastix/Elastix.py at 3e9ef490ee6a6f901daa3280af112950f6af13ec · lassoan/SlicerElastix · GitHub</a></p>

---

## Post #3 by @Vincebisca (2022-08-26 15:20 UTC)

<p>Hi ! Sorry I forgot to reply <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"><br>
You were indeed right ! I bumped into a few other issues but I managed to solve it and it work as intended now ! Thank you very much !</p>

---
